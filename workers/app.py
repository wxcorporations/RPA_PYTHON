import os
import asyncio

from dotenv import load_dotenv

from util import performace
from core.csv_file import create_fake
from use_case.use_case_filter_reports_csv import generate_reports_execute

load_dotenv()

PATH_FILE_ORIGIN = os.getenv("PATH_ORIGIN")

print('\n')

# Criando fonte de dados dinamica
asyncio.run(performace('Criacao dados fake', create_fake, [PATH_FILE_ORIGIN, 10000]))
print('\n')

# gera os relatorios
asyncio.run(performace('Criacao dos relatorios', generate_reports_execute, []))

