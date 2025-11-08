

# criar uma api com o seguinte endpoint


# - dashboard

# - get
#     listas todos os relatorios enviados com as seguintes informações
#     - quem enviou
#     - codigo de identificacao do relatório
#     - data de envio
#     - hora e minuto
#     - tamanho do arquivo
#     - total de items no arquivo
#     - link dos relatrios finais 


# - report

# - post
#     responsavel pelo envio do relatórios deve ser enviado
#     - nome de quem enviou + 4 ultimos dig do rg
#     - arquivo do tipo csv


# - get
#     responsável pelo download dos relatórios processados

#     para download sera necessario:
#     codigo de identificacao do relatorio + tipo de relatorio desejado
        
#         ex: ab34bh + enviado, ab34bh + finalizado


import os
import uuid
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename
from use_case.use_case_filter_reports_csv import generate_reports_execute, msg
from core.hash_id import get_hash
from core.csv_file import create, add_line


UPLOAD_FOLDER = '../uploads/'
ALLOWED_EXTENSIONS = {'.csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'MINHA KEY AQUI KKKKKK'


def allowed_file(filename):
    exctension = Path(filename).suffix
    return exctension in ALLOWED_EXTENSIONS
 
@app.route("/")
def hello_world():
    return "<p>Hello, fernando jose!</p>"

@app.route("/dashboard")
def dashboard():
    return f"<p>Hello, Página dashboard!</p> {escape(uuid.uuid4())}"

@app.route("/report", methods=['POST'])
def upload_file():
    if request.method == 'POST':

    
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        if not file or file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            # woner = request.form.get('nome')
            # woner_id = request.form.get('id')
            # exctension = Path(filename).suffix

            # _name = f"{app.config['UPLOAD_FOLDER']}{filename}"

            # new_name = f"{hash}-{woner_id}{exctension}"

            # create_data_dashboard_csv(new_name)

            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            
            # hash = get_hash('../uploads/.csv')

            return redirect(url_for('dashboard', name=filename))
                
        
@app.errorhandler(404)
def page_not_found(error):
    return f'rota invalida', 404



def create_data_dashboard_csv(name):
    create(f'../uploads/{name}', ['create', 'id'])


# def upload_csv():

# pego o arquivo 
# gera um hash do arquivo
# salvo o arquivo temporariamente com o nome hash gerado.

# salvar relarios com hash de prefixo

# salvar informações do arquivo.
# nome do dono
# id do dono 
# pegar total de linhas do arquivo
# id do arquivo

