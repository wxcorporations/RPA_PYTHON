import csv
import random
from faker import Faker
from pathlib import Path
from core.config import EXTENSION_EXPECTED, EXTENSION_INVALID_ERROR_MSG

fake = Faker('pt_BR')

def create(path, header):
    EXTENSION = Path(path).suffix
    if EXTENSION != EXTENSION_EXPECTED: raise ValueError(EXTENSION_INVALID_ERROR_MSG)

    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)


async def add_line(path, line):
    EXTENSION = Path(path).suffix
    if EXTENSION != EXTENSION_EXPECTED: raise ValueError(EXTENSION_INVALID_ERROR_MSG)
    
    with open(path , mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(line)


def add_multiple_lines(path, lines):
    EXTENSION = Path(path).suffix
    if EXTENSION != EXTENSION_EXPECTED: raise ValueError(EXTENSION_INVALID_ERROR_MSG)
    
    with open(path , mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        for line in range(lines): 
            writer.writerows(line)


async def create_fake(path, lines):
    statuses = ['ENVIAR', 'FINALIZAR', 'CRITICAR']

    with open(path , mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['create-at', 'description', 'cnpj', 'amount', 'movement-status'])
        
        for _ in range(lines):
            data = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
            description = fake.sentence(nb_words=8)
            cnpj = fake.cnpj()
            amount = round(random.uniform(100, 10000), 2)
            status = random.choice(statuses)
            writer.writerow([data, description, cnpj, amount, status])
        
        print('Arquivo gerando com sucesso!')
    

async def read_lines_csv(path, process):
    extension = Path(path).suffix
    total_lines = 0
    if extension != EXTENSION_EXPECTED: raise ValueError(EXTENSION_INVALID_ERROR_MSG)
    
    with open(path) as csv_file:
        for line in csv_file:
            await process(line)
            total_lines += 1

    return total_lines