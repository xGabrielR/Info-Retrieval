import os
import re
import json
import nltk
import requests
import warnings
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
from pandas.core.frame import DataFrame

from utils import BasePipeline
from utils import DB_NAME,DB_HOST,DB_PASS,DB_USER,DB_PORT


R_LIST = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L','LI',
          'LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX','LX','LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX','LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX','LXXX','LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX','XC','XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVIII','XCIX','C']

A_LIST = [
    'a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)',
    'n)', 'o)', 'p)', 'q)', 'r)', 's)', 't)', 'u)', 'v)', 'w)', 'x)', 'y)', 'z)'
]

class ScrapyCF(BasePipe):
    
    def __init__(self):
        self.page_path = 'page/Constituição.html'
        self.hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5),AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.url = 'https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-publicacaooriginal-1-pl.html'

        
    def fix_wrong_range_var(self, df1, range_var, range_value, text='texto') -> DataFrame:
        for _, row in df1.iterrows():
            if len(row[range_var]) > range_value:
                row[text] = row[range_var][range_value:].strip()
                row[range_var] = row[range_var][:range_value].strip()

        return df1
    

    def check_len_row(self, row, aux_list, append_var):
        if len(row) > 2:
            aux_list.append(
                {append_var: row[0], 'texto': ' '.join(row[1:])}
            )

        else:
            aux_list.append(
                {append_var: row[0], 'texto': row[1]}
            )

        return None
    

    def get_titles_from_camara(self) -> dict:
        pg = requests.get(url=self.url, headers=self.hdr)
        soup = BeautifulSoup(pg.text, 'html.parser')

        txt = soup.find('div', class_='textoNorma').get_text().replace('rt.', 'rt').replace('º', '.').replace('arts.', 'arts ')

        pre_txt = [k.strip() for k in nltk.tokenize.sent_tokenize(
            txt, language='portuguese'
        )]

        pre_txt = [list(filter(None, r.split('\xa0'))) for r in pre_txt]

        titles_dict = [{art[1].replace('Art', 'Art.'): ' '.join(art[0].split('\n')[:2]).strip()} for art in pre_txt if art[0].startswith('TÍTULO')]
        titles_dict = {k:v for i in titles_dict for k, v in i.items()}

        return titles_dict
    
    
    def page_extraction(self) -> list:
        soup = BeautifulSoup(open(self.page_path).read(), 'html.parser')

        source = ' '.join([k.get_text().strip() for k in soup.find_all('big')][1:])

        df_ref = pd.DataFrame(columns=['artigo', 'texto', 'paragrafo_unico', 'inciso', 'alinea', 'paragrafo'])

        full_html_page_list = soup.find_all('div', attrs={'id': 'art'})[:-1]

        full_txt_list = []
        for page in full_html_page_list:
            txt = page.get_text().replace('rt.', 'rt').replace('arts.', 'arts ').replace('\xa0', '\n').replace('\n\t', '')

            for j in range(1, 120):
                txt = txt.replace(f'{j}º', f'{j}.')

            pre_txt = [k.strip() for k in nltk.tokenize.line_tokenize(txt)]
            pre_list = [k.replace(' - ', '. ').replace(')', ').').split('.') for k in pre_txt]
            pre_list = [list(filter(None, row)) for row in pre_list]

            full_txt_list.append(pre_list)

        return full_txt_list
    

    def get_pages_data(self, list_pages) -> dict:
        full_discarted_list = []
        df_ref = pd.DataFrame(columns=['artigo', 'texto', 'paragrafo_unico', 'inciso', 'alinea', 'paragrafo'])

        for page in list_pages:
            aux_list = []
            discarted_list = []

            for i in range(0, len(page)):
                row = page[i]

                if row:  
                    if row[0].startswith('Art') and len(row) > 1:
                        self.check_len_row(row, aux_list, append_var='artigo')

                    elif row[0].startswith('§') and len(row) > 1:
                        self.check_len_row(row, aux_list, append_var='paragrafo')

                    elif row[0].startswith('Parágrafo único') and len(row) > 1:
                        self.check_len_row(row, aux_list, append_var='paragrafo_unico')

                    elif row[0] in A_LIST and len(row) > 1:
                        self.check_len_row(row, aux_list, append_var='alinea')

                    elif row[0] in R_LIST and len(row) > 1:
                        self.check_len_row(row, aux_list, append_var='inciso')

                    else: discarted_list.append(row)

            full_discarted_list.append(discarted_list)
            df_arts = pd.DataFrame(aux_list).reset_index(drop=True)

            df_ref = pd.concat([df_ref, df_arts], axis=0)

            # #Tranform df on dict*
        return {'df': df_ref, 'discarted_rows': discarted_list}
    

    def data_cleaning(self, **kwargs) -> DataFrame:
        df = kwargs['df'].reset_index(drop=True)

        df.artigo = df.artigo.fillna(method='ffill')
        df.artigo = df.artigo.apply(lambda x: x.replace('\t', '').replace(' ', '. ')+'.' )

        df.inciso = df.inciso.fillna('na')
        df.alinea = df.alinea.fillna('na')
        df.paragrafo_unico = df.paragrafo_unico.apply(lambda x: 'pu' if not pd.isna(x) else 'na')

        df.paragrafo = df.paragrafo.fillna('na')                        # Special Case
        df.paragrafo = df.paragrafo.apply(lambda x: x.replace('\t', '').replace('° do art 22 da Lei n° 8', ''))

        df.texto = [i.replace(':', '')+'.' if i.endswith(':') else i for i in [r.replace('\t', '').strip().capitalize() for r in df.texto.tolist()]]

        df = df.drop_duplicates()

        return df
    

    def data_preparation(self, clean_df) -> DataFrame:
        df = self.fix_wrong_range_var(clean_df, 'paragrafo', 5)

        df['titulo'] = np.nan

        titles_dict = self.get_titles_from_camara()

        for i, row in df.iterrows():
            if row['artigo'] in list(titles_dict.keys()):
                df.loc[df.index == i, 'titulo'] = titles_dict[row['artigo']]

        df['sigla'] = 'CF88'
        df['link']  = 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'
        df['scrapy_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df['process_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        df = df[['sigla', 'titulo', 'texto', 'artigo', 'inciso', 'alinea', 'paragrafo', 'paragrafo_unico', 
                   'link', 'scrapy_datetime', 'process_datetime']]

        return df

    
    def data_store(self, df) -> dict:
        # Add More Data Storanges Here
        
        df.to_csv(f"cf88_scrapy_{datetime.now().strftime('%Y-%m-%d')}.csv", index=False)
        df_json = json.dumps(df.to_dict(orient="records"))
        
        return df_json