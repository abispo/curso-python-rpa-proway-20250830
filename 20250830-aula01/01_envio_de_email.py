from datetime import datetime

from typing import List

import csv
import os
import sqlite3

from sqlite3 import Connection

def criar_banco_de_dados(conn: Connection):

    cursor = conn.cursor()

    sql = """
CREATE TABLE IF NOT EXISTS sensores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    leitura_chuva TEXT NULL,
    leitura_temperatura TEXT NULL,
    leitura_umidade TEXT NULL
);"""

    cursor.execute(sql)

def salvar_dados_na_tabela(conn: Connection, nome_arquivo: str):
    
    codigo_sensor, tipo_leitura, _ = arquivo.split("_")

if __name__ == "__main__":

    connection_string = os.path.join(os.getcwd(), "db.sqlite3")
    
    if os.path.exists(connection_string):
        os.remove(connection_string)

    conexao = sqlite3.connect(connection_string)

    criar_banco_de_dados()
    
    pasta_arquivos = os.path.join(os.getcwd(), "sensores_dia")
    arquivo_zip = f"sensores_data_{datetime.now().strftime('%Y%m%d')}"

    variavel = 1
    variavel = "Python"

    arquivos: List[str] = []

    for caminho, _, arquivos in os.walk(pasta_arquivos):
        for arquivo in arquivos:
            salvar_dados_na_tabela(conexao, arquivo)