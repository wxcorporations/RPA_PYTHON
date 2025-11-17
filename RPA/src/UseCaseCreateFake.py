import random
from FileCsv import FileCsv
from config import HEADER_COLUMNS
from FakeDataReport import FakeDataReport, template_csv_fake

class UseCaseCreateFake:
    def __init__(self, path_output, total_files):
        self.total_file = total_files
        self.output = path_output
        
    def execute(self):
        for index in range(self.total_file):
            total_itens = random.randrange(10, 1_000_000)

            data = FakeDataReport.create(template_csv_fake, total_itens)
            FileCsv.create(f"{self.output}relatorio-origem-{index}.csv", HEADER_COLUMNS, data)

            print('arquivo gerado com sucesso')
            print('-------------------------------------')