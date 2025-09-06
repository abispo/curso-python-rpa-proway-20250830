import os
import requests
import sqlite3

from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime
from sqlite3 import Connection
from typing import List

def configurar_banco_de_dados(connection: Connection):
    cursor = connection.cursor()
    sql = """
CREATE TABLE IF NOT EXISTS tb_nivel_itajai_acu_blumenau(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hora_leitura TEXT NOT NULL,
    nivel TEXT NOT NULL,
    variacao TEXT NOT NULL
);"""

    cursor.execute(sql)

def salvar_dados_na_tabela(connection: Connection, dados: List[str]):
    cursor = connection.cursor()
    sql = "INSERT INTO tb_nivel_itajai_acu_blumenau(hora_leitura, nivel, variacao) VALUES (?, ?, ?)"
    cursor.execute(sql, dados)
    connection.commit()
    cursor.close()

def limpar_dados(tags: List[Tag]) -> List[str]:
    hora_leitura = datetime.strptime(
        tags[0].get_text().strip(), "%d/%m/%Y %H:%M"
    ).strftime("%Y-%m-%d %H:%M:%S")
    nivel = tags[1].get_text().strip()
    variacao = tags[2].get_text().strip()

    return [hora_leitura, nivel, variacao]

if __name__ == "__main__":
    connection_string = os.path.join(os.getcwd(), "dbmedidas.sqlite3")

    if os.path.exists(connection_string):
        os.remove(connection_string)

    conexao = sqlite3.connect(connection_string)

    configurar_banco_de_dados(conexao)

    url = "https://alertablu.blumenau.sc.gov.br/d/nivel-do-rio"
    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")

    # Localizar a tag title que possui os dados de leitura do rio
    dados = soup.find("table", id="river-level-table").find("tbody")

    # Retornar todas as linhas com dados na tabela de leitura do rio
    linhas = dados.find_all("tr")

    for linha in linhas:
        colunas = linha.find_all("td")

        leituras = limpar_dados(colunas)
        salvar_dados_na_tabela(conexao, leituras)
        print(f"Dados salvos na leitura de {leituras[0]}.")
