import os
from dotenv import load_dotenv

from core.config import HEADER_COLUMNS
from core.reports_csv import manager_data_reports
from core.csv_file import create, read_lines_csv

load_dotenv()

PATH_FILE_ORIGIN = os.getenv("PATH_ORIGIN")

PATH_FILE_SENT = os.getenv("OUT_PUT_REPORT_SENT")
PATH_FILE_ERROR = os.getenv("OUT_PUT_REPORT_ERROR")
PATH_FILE_FINISH = os.getenv("OUT_PUT_REPORT_FINISH")

async def generate_reports_execute(hash):
    path_sent = f'{PATH_FILE_SENT}{hash}-sent.csv'
    path_error = f'{PATH_FILE_ERROR}{hash}-error.csv'
    path_finish = f'{PATH_FILE_FINISH}{hash}-finish.csv'


    def handle_data_reports (data):
        return manager_data_reports(data, path_sent, path_error, path_finish)


    for _path in [path_sent, path_error, path_finish]: 
        create(_path, HEADER_COLUMNS)

    await read_lines_csv(PATH_FILE_ORIGIN, handle_data_reports)

    print('====================     relatorios criados       ========================')


# async def generate_reports_execute():

#     def handle_data_reports (data):
#         return manager_data_reports(data, PATH_FILE_SENT, PATH_FILE_ERROR, PATH_FILE_FINISH)


#     for _path in [PATH_FILE_SENT, PATH_FILE_ERROR, PATH_FILE_FINISH]: 
#         create(_path, HEADER_COLUMNS)

#     await read_lines_csv(PATH_FILE_ORIGIN, handle_data_reports)

#     print('====================     relatorios criados       ========================')


def msg():
    print("======================= msg com sucesso ============================")