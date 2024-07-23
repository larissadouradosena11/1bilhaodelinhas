from csv import reader
from collections import defaultdict
import time

from pathlib import Path

path_do_txt = 'data\measurements.txt'

def processar_temperaturas(path_do_txt: Path):
    print("Iniciando o processamento do arquivo.")

    start_time = time.time() #Tempo do Inicio

    temperatura_por_station = defaultdict(list)

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)

    print("Dados carregados. Calculando estatisticas...")
    

    #Dicionário para armazenar os resultados calculados
    results = {}

    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)
    
    print("Estatistica calculada. Ordenando...")
    #Ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    end_time = time.time()
    print(f"Processamento concluído em {end_time - start_time: .2f} segundos.")

#Substitua "data/measurements.txt" pelo caminho correto do seu arquivo
if __name__ == "__main__":
    path_do_txt: Path == Path("data\measurements.txt")
    resultados = processar_temperaturas(path_do_txt)
