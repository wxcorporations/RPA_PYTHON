import time
import os
import queue
import threading
from pathlib import Path
from math import floor
from multiprocessing import Pool

def extension_valid(path, allowed_extensions):
    exctension = Path(path).suffix    
    return exctension in allowed_extensions


def msg():
    print('======================== pacote util =============================')



# Afuncao sempre deve retornar o valor processado
# args pode ser homitido, caso preceise passar parametros para sua funcao passe detro de uma lista para args
def run_in_threads(**kwargs):
    try:
        args = kwargs.get('args', ())
        func = kwargs.get('func', None)
        threads_factor = kwargs.get('threads', 0.7)
        
        result_shared = queue.Queue()
        cpu_threads = floor(os.cpu_count() * threads_factor)
        
        threads_list = []
        result = []

        def result_list(share):
            if args:
                share.put(func(*args))
            else:
                share.put(func())
        
        # Se for async, o correto é usar asyncio.run ou loop e threading não é recomendado para async.
        # Aqui só exemplo para sync/threading.
        __args = (result_shared,)

        for _ in range(cpu_threads):            
            t = threading.Thread(target=result_list, args=__args)
            threads_list.append(t)
            t.start()

        for t in threads_list:
            t.join()

        while not result_shared.empty():
            item = result_shared.get()
            result.append(item)
        
        return result

    except ValueError as error:
        print('Error: =====================> ')
        print(error)
    

async def performace_async(label, callback, arg=None):
    init = time.time()
    
    print(f'Iniciando analise de performace: {label}!')
    
    if arg is None:
        await callback()
    else: 
        await callback(*arg)
    
    print(f'Tempo de execuçao = {time.time() - init}')
    
    
def performace(label, callback, arg=None):
    print(f'Iniciando analise de performace: {label}!')
    init = time.time()

    if arg is None:
        callback()
    else: 
        callback(*arg)
    
    print(f'Tempo de execuçao = {time.time() - init}')
    
    
    
def multi_process(func, round=1):
    with Pool() as pool:
        return pool.map(func, range(round))