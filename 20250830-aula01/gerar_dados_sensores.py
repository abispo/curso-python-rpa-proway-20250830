import csv
import random
import string
from datetime import datetime
import os

if __name__ == "__main__":

    # Configurações
    tipos_sensores = ['umidade', 'temperatura', 'chuva']
    num_sensores = 5        # Quantos sensores gerar
    intervalo_horas = 1     # Intervalo entre medições
    data_hoje = datetime.now().strftime('%Y%m%d')
    output_folder = 'sensores_dia'

    # Cria pasta de saída
    os.makedirs(output_folder, exist_ok=True)

    # Função para gerar ID do sensor LLNNN
    def gerar_id_sensor():
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=3))
        return letras + numeros

    # Função para gerar valores simulados por tipo de sensor
    def gerar_valor(sensor_tipo):
        if sensor_tipo == 'umidade':
            return round(random.uniform(20, 90), 1), '%'
        elif sensor_tipo == 'temperatura':
            return round(random.uniform(15, 35), 1), '°C'
        elif sensor_tipo == 'chuva':
            return round(random.uniform(0, 20), 1), 'mm'
        else:
            return 0, ''

    # Gera arquivos para cada sensor e tipo
    for _ in range(num_sensores):
        sensor_id = gerar_id_sensor()
        
        for sensor_tipo in tipos_sensores:
            filename = f"{sensor_id}_{sensor_tipo}_{data_hoje}.csv"
            filepath = os.path.join(output_folder, filename)
            
            # Gera medições do dia (somente hora: 00:00 até 23:00)
            dados = []
            for hora in range(24):
                valor, unidade = gerar_valor(sensor_tipo)
                timestamp = f"{hora:02d}:00:00"
                dados.append([timestamp, valor, unidade])
            
            # Escreve arquivo CSV com separador ;
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['timestamp', 'valor', 'unidade'])
                writer.writerows(dados)

    print(f"✅ Arquivos gerados na pasta '{output_folder}' para o dia {data_hoje}")
