
import os
import random
import requests
from config import DATA_ORIGIN_FOLDER


def name_file_dinamic():
    return f'arquivo-{random.randrange(start=1, stop=100)}-{random.randrange(start=1, stop=100)}.csv'

def send_file(path):
    url = 'http://127.0.0.1:5000/report'  # Replace with your target URL

    data = { 'name': f'fernando-{random.randrange(start=1, stop=100)}' }

    name = name_file_dinamic()
    
    files = { 'file': (name, open(path, 'rb'), 'text/csv') }

    response = requests.post(url, data=data, files=files)

    print(response.status_code)
    print(response.text)
    


class UseCaseUploadFilesAuto:
    def __init__(self):
        print('iniciando')
    
    def execute(self): 
        arquivos = os.listdir(DATA_ORIGIN_FOLDER)
        
        for file in arquivos:
            path_file = f'{DATA_ORIGIN_FOLDER}{file}'
            send_file(path_file)
        

run = UseCaseUploadFilesAuto()

run.execute()