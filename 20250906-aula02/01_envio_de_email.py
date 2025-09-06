from datetime import datetime

from typing import List

import csv
import os
import sqlite3
import zipfile

from sqlite3 import Connection
from openpyxl import Workbook

def criar_banco_de_dados(conn: Connection):

    cursor = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS leituras_sensores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_sensor TEXT NOT NULL,
        leitura_chuva TEXT NOT NULL,
        leitura_temperatura TEXT NOT NULL,
        leitura_umidade TEXT NOT NULL,
        data_hora TEXT NULL
    );"""
    cursor.execute(sql)

def salvar_dados_na_tabela(conn: Connection, nome_arquivo: str, arquivo_csv: csv.DictReader):
    
    cursor = conn.cursor()

    for linha in arquivo_csv:
        sql = f"""
            INSERT INTO leituras_sensores(
                codigo_sensor,
                data_hora,
                leitura_chuva,
                leitura_temperatura,
                leitura_umidade
            ) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sql, tuple(linha.values()))
        conn.commit()
        
def gerar_planilha(conn: Connection):
    
    wb = Workbook()
    cursor = conn.cursor()
    wb.remove(wb.active)

    result = cursor.execute("SELECT DISTINCT codigo_sensor FROM leituras_sensores").fetchall()

    for sensor in result:
        ws = wb.create_sheet(title=sensor[0])
        ws.append(["data_hora", "chuva", "temperatura", "umidade"])
        ws.insert_rows(2, 1)

        sql = """
            SELECT
                data_hora,
                leitura_chuva,
                leitura_temperatura,
                leitura_umidade
            FROM leituras_sensores
            WHERE codigo_sensor = ?"""

        result = cursor.execute(sql, sensor).fetchall()

        for linha in result:
            ws.append(linha)
            print(f"Dados para o sensor {sensor} gerados com sucesso.")

    wb.save(os.path.join(os.getcwd(), "dados_sensores.xlsx"))

def compactar_arquivo(caminho_arquivo: str):
    arquivo_saida = "dados_sensores.zip"

    with zipfile.ZipFile(arquivo_saida, 'w', compression=zipfile.ZIP_DEFLATED) as zfile:
        zfile.write(caminho_arquivo, arcname=os.path.basename(caminho_arquivo))

if __name__ == "__main__":

    connection_string = os.path.join(os.getcwd(), "db.sqlite3")
    
    if os.path.exists(connection_string):
        os.remove(connection_string)

    conexao = sqlite3.connect(connection_string)

    criar_banco_de_dados(conexao)
    
    arquivo_leituras = os.path.join(os.getcwd(), "leituras.csv")
    arquivo_zip = f"sensores_data_{datetime.now().strftime('%Y%m%d')}"

    arquivos: List[str] = []

    with open(arquivo_leituras, 'r', encoding="utf-8") as _arquivo:
        arquivo_csv = csv.DictReader(_arquivo, delimiter=';')
        salvar_dados_na_tabela(conexao, arquivo_leituras, arquivo_csv)

    gerar_planilha(conn=conexao)
    compactar_arquivo(caminho_arquivo="dados_sensores.xlsx")