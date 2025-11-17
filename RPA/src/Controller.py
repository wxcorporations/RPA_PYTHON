import asyncio
import time
from db import DataBase
from FileCsv import FileCsv 
from UseCaseCreateReports import UseCaseCreateReports
# from csv_file import create, add_multiple_lines, add_line
from config import REPORT_FOLDER, HEADER_TABLE_PENDING, UPLOAD_FOLDER, MANAGER_FOLDER

file_pending = f"{MANAGER_FOLDER}pendente.csv"
file_erro_process = f"{MANAGER_FOLDER}erros.csv"

list_error = []

DB = DataBase()

def scheduled_task(func, delay=5):
    while True:
        func()
        time.sleep(delay)


def get_data_pending():
    return DB.get_pendings()

def convert_data_db_to_csv_data(data_db):
    tmp = []
    for row in data_db:
        tmp.append(list(row))
    return tmp

def handle_data_pending():
    itens_by_db = get_data_pending()
    itens_in_memory = convert_data_db_to_csv_data(data_db=itens_by_db)
    
    # FileCsv.add_lines(path=file_pending, values=itens_in_memory)
    
    return itens_in_memory

def use_case_process_file():
    list_file_finish = []
    print('=================== inicio callback ============================')
#     verfica se arquivo da pasta manager pendente esta vazio

    itens_in_memory = handle_data_pending() or []

#   sim 
    if len(itens_in_memory):
        
        print('============== processar arquivo da lista ===================')
        # intera itens
        for item in itens_in_memory:
            print('item ================================= ', item)
            
            try:
                print(item, '======================')
            #     processa item

                name = item[0]
                
                createReports = UseCaseCreateReports(
                    dir_upload=f"{UPLOAD_FOLDER}",
                    out_report=REPORT_FOLDER,
                    name_file=name
                )
                
                createReports.execute()
                
                list_file_finish.append(name)
                
        #     deu erro ao processar
            except ValueError as error:
        #         inclui item no arquivo erros da pasta manager
                FileCsv.add_line(path=file_erro_process, value=item)
                print(error)
        #         vai para o proximo item
                continue
        
        
        for item_processed in list_file_finish:
            DB.update_file_id(hash=item_processed)
        
        # FileCsv.create(path=file_pending)
        
        #     gera reports
        #     acessar o banco na tabela pending
        #     atualizar os status dos itens para 0


        # remove todos itens do arquivo pendente da pasta manager


# criar um rotina "polling" com intervalo de 60 segundo

scheduled_task(use_case_process_file, 5)

 