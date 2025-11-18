import csv
from faker import Faker
from pathlib import Path
from config import ENCODE_FILE

fake = Faker('pt_BR')

class FileCsv:
        
    @staticmethod
    def total_itens(path):
        count = 0
        with open(path, mode='r', encoding=ENCODE_FILE) as file:
            for _ in file:
                count += 1    
        return count

    @staticmethod
    def create(path, header=None, data=None):
        with open(path, mode='w', encoding=ENCODE_FILE) as file:
            csv_file = csv.writer(file)
            
            if header != None:
                csv_file.writerow(header)
            
            if data != None:
                csv_file.writerows(data)
    
    # Este metodo espera uma lista com string com valores de cada coluna.
    @staticmethod
    def add_line(path, value):
        with open(path, mode='a', encoding=ENCODE_FILE) as file:
            write = csv.writer(file)
            write.writerow(value)
            
        
    # este metodo espera uma matris de string com valores das colunas.
    @staticmethod
    def add_lines(path, values):
        with open(path, mode='a', encoding=ENCODE_FILE) as file:
            write = csv.writer(file)
            write.writerows(values)
    
    @staticmethod
    def read_lines(path, func):
        with open(path, mode='r', encoding=ENCODE_FILE) as file:
            for row in file:
                func(row)
    
    @staticmethod
    async def read_lines_async(path, func):
        with open(path, mode='r', encoding=ENCODE_FILE) as file:
            for row in file:
                await func(row)
    