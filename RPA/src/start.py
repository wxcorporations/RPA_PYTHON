import subprocess
from UseCaseCreateFake import UseCaseCreateFake
from config import DATA_ORIGIN_FOLDER, REPORT_FOLDER, UPLOAD_FOLDER

def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Error =====================> : {e}")
        return
    
def clean_store():
    run_command(f"rm -rf ./reports.db")
    run_command(f"rm -rf {DATA_ORIGIN_FOLDER}*.csv")  
    run_command(f"rm -rf {REPORT_FOLDER}*.csv")  
    run_command(f"rm -rf {UPLOAD_FOLDER}*.csv")

clean_store()
run_command(".venv/bin/python -m flask --app ./src/api --debug run")


# gerar os aquivos fakes
fakes = UseCaseCreateFake(path_output=DATA_ORIGIN_FOLDER, total_files=5)
fakes.execute()


# subir serviço processador
run_command("python3 ./src/Controller.py")


# subir serviço upload automatico
run_command("python3 ./src/UseCaseUploadFilesAuto.py")


