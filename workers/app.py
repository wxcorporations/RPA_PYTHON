import os
import asyncio

from dotenv import load_dotenv

from util import performace
from core.csv_file import create_fake
from use_case.use_case_filter_reports_csv import generate_reports_execute

load_dotenv()

PATH_FILE_ORIGIN = os.getenv('PATH_ORIGIN')
TOTAL_LINE = os.getenv('TOTAL_LINES_ORIGIN')

print('\n')

# Criando fonte de dados dinamica
# asyncio.run(performace('Criacao dados fake', create_fake, [PATH_FILE_ORIGIN, int(TOTAL_LINE)]))
print('\n')

async def handle_report():
    await generate_reports_execute('0fc3048fb55cb7f83eef29c0fc0dcc43')

# gera os relatorios
asyncio.run(performace('Criacao dos relatorios', handle_report, []))

