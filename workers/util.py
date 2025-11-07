import time

async def performace(label, callback, arg):
    print(f'Iniciando analise de {label}!')

    init = time.time()
    await callback(*arg)
    finish = time.time()
    
    print(f'Tempo de execuçao = {finish - init}')
