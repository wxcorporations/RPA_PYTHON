# Usa a imagem oficial do Python 3 como base (já inclui pip3)
FROM python:3

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# (Opcional) Instala dependências do projeto
# RUN pip install --no-cache-dir -r requirements.txt

# Define o comando padrão ao executar o container
CMD ["python", "seu_arquivo.py"]
