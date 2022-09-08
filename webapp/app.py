import streamlit as st
from elasticsearch import Elasticsearch
from utils import E_CLOUD_HOST, E_CLOUD_USER, E_CLOUD_PSWD

st.set_page_config(page_title="Info-Law", page_icon="⚖️")

class InfoLawApp(object):
    def __init__(self):
        self.tit_style = "font-size:10px"
        self.div_style = "background-color:rgb(0,0,0);padding:10px;font-family:'Times New Roman',serif;color:rgb(255, 255, 255)"

    def connect_to_elastic(self):
        try:
            es = Elasticsearch(
                use_ssl=True,
                hosts=E_CLOUD_HOST, 
                http_auth=(E_CLOUD_USER, E_CLOUD_PSWD)
                #verify_certs=True,
            )
            return es
        except:
            return None

    def app_header(self) -> tuple:
        st.title("👨‍⚖️ | Information Law")
        st.write('___')
        text = st.text_input('Digite o Texto Abaixo...✏️')

        st.sidebar.header('Filtros por Pesquisa & Tipo de Lei')
        st.sidebar.write('___')

        law_info = st.sidebar.radio(
                    "◪ Selecione a Categoria da Lei",
                    ['CF88', 'CLT',]# 'CPC', 'Todas']
        ).lower()

        search_info = st.sidebar.radio(
                    "◩ Tipos de Consultas",
                    ["Específica", "Similares", "Por Palavra"]
        ).lower()

        return (text, law_info, search_info)

    def get_query_type(self, text, search_info, parsed=False) -> dict:
        map_query_type = {"específica":0, "similares":1, "por palavra":2}[search_info] 
        if parsed:
            if len(text[0]) >= 3 and len(text[1]) >= 3:
                query = {"query": { "bool": { "must": [ {"wildcard": { "texto": { "value": f"{text[0][:3]}*" } } }, {"wildcard": { "texto": { "value": f"{text[1][:3]}*" } } } ] } } }
                return query
            else:
                query = {"query": { "bool": { "must": [ {"wildcard": { "texto": { "value": f"{text[0][:1]}*" } } }, {"wildcard": { "texto": { "value": f"{text[1][:1]}*" } } } ] } } }
                return query
        else:
            query_list = [
                {"query": { "match_phrase_prefix": { "texto": { "query": f"{text}", "slop":10 } } } },
                {"query": { "fuzzy": { "texto": { "value": f"{text}", "fuzziness": 2 } } } },
                {"query": { "match": { "texto": f"{text}" } } },
            ]

            return query_list[map_query_type]

    def parse_query_resuls(self, query_result) -> str:
        if query_result:
            try:
                html_rows = ' '.join([
                    f"""<ti style={self.tit_style}>{row['titulo']}</ti><p><a href="{row['link']}">{row['padrao']}</a>: {row['texto']}</p>""" 
                    for row in query_result
                ])

                html_text = f"""
                <div style="{self.div_style}">
                    {html_rows}
                </div>
                """
            except:
                html_text = f"""
                    <p>Não foi encontrado <b>NENHUM</b> resultado para a pesquisa!</p>
                """
        else:
            html_text = f"""
                <p>Não foi encontrado <b>NENHUM</b> resultado para a pesquisa!</p>
            """

        return html_text

    def make_elastic_search(self, es, text, law_info, search_info) -> str: # Add anothers Law's (CF, CPC...)
        if es:
            query_body = self.get_query_type(text, search_info)
            query_result = es.search(index=f"{law_info}-law", body=query_body)
            query_result = [r['_source'] for r in query_result['hits']['hits']]

            if search_info == 'similares' and not query_result:
                parsed_text = text.split()
                if len(parsed_text) >= 2:
                    query_body = self.get_query_type(parsed_text, search_info, parsed=True)
                    query_result = es.search(index=f"{law_info}-law", body=query_body)
                    query_result = [r['_source'] for r in query_result['hits']['hits']]

                    return self.parse_query_resuls(query_result)
        
            return self.parse_query_resuls(query_result)

        else:
            st.write("Olá, não foi possível estabelecer uma conexão com o Servidor Elastic. 😔")
            return None

if __name__ == '__main__':
    il = InfoLawApp()

    es = il.connect_to_elastic()

    text, law_info, search_info = il.app_header()

    if text:
        results = il.make_elastic_search(es, text, law_info, search_info)

        if results: 
            st.write(results, unsafe_allow_html=True)

# Test this query in future:
#{"query": { "bool":{ "should": [ {"fuzzy": { "texto": { "value": "justiça",  "fuzziness": 2}}}  ], "must": [ { 
#   "bool": { "should": [ {"wildcard": { "texto": { "value": "*justica social*", "case_insensitive": false } }} ] }} ] } } }