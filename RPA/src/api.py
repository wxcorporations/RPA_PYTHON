
import os
import re
import uuid
import asyncio
import sqlite3

from db import DataBase
from markupsafe import escape
from utils import extension_valid
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import Flask, flash, request, redirect, url_for
from Hash import Hash

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# TODO: ADD KEY NO .ENV
app.secret_key = 'MINHA KEY AQUI KKKKKK'
 
@app.route("/")
def hello_world():
    return "<p>Hello, fernando jose!</p>"

@app.route("/dashboard")
def dashboard():
     return f"<p>Hello, Página dashboard!</p> {escape(uuid.uuid4())}"

@app.route("/report", methods=['POST'])
def upload_file():
    try:
        if request.method == 'POST':
            DB = DataBase()
        
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            
            file = request.files['file']

            if not file or file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if extension_valid(file.filename, ALLOWED_EXTENSIONS):
                filename = secure_filename(file.filename)
                name_tmp = os.path.join(UPLOAD_FOLDER, filename)
                
                file.save(name_tmp)
                hash = Hash.by_file(name_tmp)

                os.rename(name_tmp, f"{UPLOAD_FOLDER}{hash}.csv")
                
                woner = request.form.get('name')
                
                DB.save_file(hash, woner, 0)
                
                # RETORNA USUARIO PAR PAGINA DE LISTAGEM
                return redirect(url_for('dashboard', name=filename))

        else:
            return 'metodo nao permitido', 400
        
    # TODO: TRATAR O ERRO RETORNADO DO SGBD - CASO SEJA ENVIADO O MESMO AQUIVO DEVE SER RETRONADO ERRO DE ARQUIVO DUPLICADO.
    except sqlite3.Error as e:
        # Captura o erro específico do SQLite
        print(f"Ocorreu um erro no banco de dados: {e}")
        # Opcional: rollback em caso de erro para não deixar a transação inconsistente
        DB.rollback()
        
        return e, 500
                
        
@app.errorhandler(404)
def page_not_found(error):
    return f'rota invalida', 404
