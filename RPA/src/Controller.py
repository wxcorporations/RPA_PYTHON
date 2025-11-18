import time
from db import DataBase
from FileCsv import FileCsv 
from UseCaseCreateReports import UseCaseCreateReports
from config import REPORT_FOLDER, UPLOAD_FOLDER, MANAGER_FOLDER

file_erro_process = f"{MANAGER_FOLDER}erros.csv"
list_error = []

DB = DataBase()

def scheduled_task(func, delay=5):
    while True:
        print('Executando rotina agendada...')
        print('===================================')    
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
    
    return itens_in_memory

def use_case_process_file():
    list_file_finish = []
    itens_in_memory = handle_data_pending() or []

    if len(itens_in_memory):
        for item in itens_in_memory:
            try:
                print('item:', item)
                name = item[0]
                
                create_reports = UseCaseCreateReports(
                    dir_upload=f"{UPLOAD_FOLDER}",
                    out_report=REPORT_FOLDER,
                    name_file=name
                )
                
                create_reports.execute()
                list_file_finish.append(name)
                
            except ValueError as error:
                FileCsv.add_line(path=file_erro_process, value=item)
                print(error)
                continue
        
        
        for item_processed in list_file_finish:
            DB.update_file_id(hash=item_processed)
    
scheduled_task(use_case_process_file, 5)