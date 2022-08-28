import os
from time import sleep
from datetime import datetime

def cf88_workflow():
    workflow = ScrapyCF()

    DATE = datetime.now().strftime("%Y-%m-%d")
    FILE = open(f'logs/cf88/cf88_scrapy_logs_{DATE}.txt', 'a')

    print(f'\n[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Starting ScrapyCF Class\n', file=FILE)

    list_pages = workflow.page_extraction()
    sleep(1)
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Ended Page Extraction', file=FILE)

    raw_data = workflow.get_pages_data(list_pages)
    sleep(1)
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Ended Get Pages Data', file=FILE)

    clean_data = workflow.data_cleaning(df=raw_data['df'])
    sleep(1)
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Ended Data Cleaning', file=FILE)

    prepared_data = workflow.data_preparation(clean_data)
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Ended Data Preparation', file=FILE)

    json_data = workflow.data_store(prepared_data)
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Ended Data Load', file=FILE)

    print(f'\n[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] | Starting ScrapyCF Class\n', file=FILE)

if __name__ == '__main__':
    
    if not os.path.exists('logs'): # Simple Logs :D
        os.makedirs('logs/cf88/')
    
    cf88_workflow()