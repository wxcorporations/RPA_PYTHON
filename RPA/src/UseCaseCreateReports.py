import re

from db import DataBase
from pathlib import Path
from FileCsv import FileCsv
from config import HEADER_COLUMNS

        
class UseCaseCreateReports:
    def __init__(self, dir_upload, out_report, name_file):
        self.out_report = out_report
        self.name_file = name_file
        self.dir_upload = dir_upload
        self.out_sent = f'{out_report}{name_file}-sent.csv'
        self.out_error = f'{out_report}{name_file}-error.csv'
        self.out_finish = f'{out_report}{name_file}-finish.csv'
        
        self.__create_reforts()
    
    def __create_reforts(self):
        for path in [self.out_sent, self.out_error, self.out_finish]:
            FileCsv.create(path, HEADER_COLUMNS)
    
    def __manager_reports(self, data):
        is_sent = re.search('\,ENVIAR$', data)
        is_error = re.search('\,CRITICAR$', data)
        is_finish = re.search('\,FINALIZAR$', data)
        
        data_to_list = data.replace("\n", "").split(',')

        if is_sent: FileCsv.add_line(self.out_sent, data_to_list)
        if is_error: FileCsv.add_line(self.out_error, data_to_list)
        if is_finish: FileCsv.add_line(self.out_finish, data_to_list)
    
    def __save_report_inner_data_base(self):
        sent = [ FileCsv.total_itens(self.out_sent), Path(self.out_sent).stat().st_size, 1 ]
        error = [ FileCsv.total_itens(self.out_error), Path(self.out_error).stat().st_size, 3 ] 
        finish = [ FileCsv.total_itens(self.out_finish), Path(self.out_finish).stat().st_size, 2 ]
        
        DB = DataBase()
        
        for data in [sent, error, finish]:
            itens, size, category = data
            DB.save_report(name=self.name_file, itens=itens, size=size, category=category)
            
        DB.connect.close()
    
    def execute(self):
        try:
            print('Iniciando processamento:')
            print('---------------------------------------------')
            path_file_process = f'{self.dir_upload}{self.name_file}.csv'
            FileCsv.read_lines(path_file_process, self.__manager_reports)
            
            self.__save_report_inner_data_base()
            print('Relatorios criados com sucesso! \n')
            print('---------------------------------------------')
            
        except ValueError:
            raise TypeError('Não foi possivel gerar os relatorios')