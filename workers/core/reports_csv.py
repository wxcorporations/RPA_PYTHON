import re
from core.csv_file import add_line

async def manager_data_reports(data, out_sent, out_error, out_finish):
    is_sent = re.search('\,ENVIAR$', data)
    is_error = re.search('\,CRITICAR$', data)
    is_finish = re.search('\,FINALIZAR$', data)
    
    data_to_list = data.replace("\n", "").split(',')

    if is_sent: await add_line(out_sent, data_to_list)
    if is_error: await add_line(out_error, data_to_list)
    if is_finish: await add_line(out_finish, data_to_list)