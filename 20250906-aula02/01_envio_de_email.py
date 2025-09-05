from datetime import datetime

from typing import List

import csv
import os
import sqlite3

from sqlite3 import Connection
from openpyxl import Workbook

def criar_banco_de_dados(conn: Connection):

    cursor = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS sensores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE NOT NULL
    );"""
    cursor.execute(sql)

    sql = """CREATE TABLE IF NOT EXISTS leituras_chuva(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id INTEGER NOT NULL,
        valor TEXT NULL,
        FOREIGN KEY(sensor_id) REFERENCES sensores(id)
    );"""
    cursor.execute(sql)

    sql = """CREATE TABLE IF NOT EXISTS leituras_temperatura(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id INTEGER NOT NULL,
        valor TEXT NULL,
        FOREIGN KEY(sensor_id) REFERENCES sensores(id)
    );"""
    cursor.execute(sql)

    sql = """CREATE TABLE IF NOT EXISTS leituras_umidade(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id INTEGER NOT NULL,
        valor TEXT NULL,
        FOREIGN KEY(sensor_id) REFERENCES sensores(id)
    );
    """
    cursor.execute(sql)

def salvar_dados_na_tabela(conn: Connection, nome_arquivo: str, arquivo_csv: csv.DictReader):
    
    codigo_sensor, tipo_leitura, _ = nome_arquivo.split("_")
    cursor = conn.cursor()

    sql = f"SELECT id, codigo FROM sensores"
    result = cursor.execute(sql).fetchall()

    dicionario_sensores = {}

    for item in result:
        dicionario_sensores.update({item[1]: item[0]})

    for linha in arquivo_csv:
        if codigo_sensor not in dicionario_sensores.keys():
            cursor.execute(f"INSERT INTO sensores(codigo) VALUES (?)", (codigo_sensor,))
            conn.commit()
            dicionario_sensores.update({codigo_sensor: cursor.lastrowid})

        sensor_id = dicionario_sensores.get(codigo_sensor)
        sql = f"INSERT INTO leituras_{tipo_leitura}(sensor_id, valor) VALUES (?, ?)"
        cursor.execute(sql, (sensor_id, linha.get('valor')))
        conn.commit()
        
def gerar_planilha(conn: Connection):
    
    wb = Workbook()
    cursor = conn.cursor()
    wb.remove(wb.active)

    result = cursor.execute("SELECT codigo FROM sensores ORDER BY codigo").fetchall()
    for codigo in result:
        ws = wb.create_sheet(title=codigo[0])

        ws.append(["chuva", "temperatura", "umidade"])

        sql = """
            SELECT
                s.codigo AS sensor,
                c.valor AS chuva,
                t.valor AS temperatura,
                u.valor AS umidade
            FROM sensores s
            INNER JOIN leituras_chuva c
                ON s.id = c.sensor_id
            INNER JOIN leituras_temperatura t
                ON s.id = t.sensor_id
            INNER JOIN leituras_umidade u
                ON s.id = u.sensor_id
            ORDER BY s.codigo;"""
        result = cursor.execute(sql).fetchall()

        print(result)

    wb.save(os.path.join(os.getcwd(), "dados_sensores.xlsx"))

if __name__ == "__main__":

    connection_string = os.path.join(os.getcwd(), "db.sqlite3")
    
    if os.path.exists(connection_string):
        os.remove(connection_string)

    conexao = sqlite3.connect(connection_string)

    criar_banco_de_dados(conexao)
    
    pasta_arquivos = os.path.join(os.getcwd(), "sensores_dia")
    arquivo_zip = f"sensores_data_{datetime.now().strftime('%Y%m%d')}"

    arquivos: List[str] = []

    for caminho, _, arquivos in os.walk(pasta_arquivos):
        for arquivo in arquivos:
            with open(os.path.join(caminho, arquivo), 'r', encoding="utf-8") as _arquivo:

                arquivo_csv = csv.DictReader(_arquivo, delimiter=';')
                salvar_dados_na_tabela(conexao, arquivo, arquivo_csv)

    gerar_planilha(conn=conexao)