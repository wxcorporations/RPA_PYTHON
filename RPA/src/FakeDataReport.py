import random
from faker import Faker
from utils import multi_process
 
fake = Faker('pt_BR')

def template_csv_fake(_):
    return [
        fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        fake.sentence(nb_words=8),
        fake.cnpj(),
        round(random.uniform(100, 10000), 2),
        random.choice(['ENVIAR', 'FINALIZAR', 'CRITICAR'])
    ]
    

class FakeDataReport:
    @staticmethod
    def create(template, limit):
        return multi_process(template, limit)
        