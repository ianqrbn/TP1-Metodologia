import time
import json
import os
import csv
import sys
import glob


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algoritmos import medir_performance, cocktail_sort, selection_sort, bubble_sort, insertion_sort

# --- Configurações do Experimento ---
REPETICOES = 10 
ALGORITMOS = {
    "Cocktail Sort (Proposto)": cocktail_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
}
PASTA_DADOS = "DADOS"
PASTA_RESULTADOS = "RESULTADOS"
OUTPUT_FILE = f"{PASTA_RESULTADOS}/resultados_experimentais.csv"

def criar_pastas():
    if not os.path.exists(PASTA_RESULTADOS):
        os.makedirs(PASTA_RESULTADOS)
        print(f"Pasta '{PASTA_RESULTADOS}/' criada.")

def carregar_dados():
    entradas = {}
    caminhos = glob.glob(f"{PASTA_DADOS}/*.json")
    
    for caminho in caminhos:
        try:
            nome_arquivo = os.path.basename(caminho).replace('.json', '')
            partes = nome_arquivo.split('_N')
            cenario = partes[0]
            tamanho = int(partes[1])
            
            with open(caminho, 'r') as f:
                lista = json.load(f)
                entradas[(tamanho, cenario)] = lista
                
        except Exception as e:
            print(f"Erro ao carregar {caminho}: {e}")
            
    return entradas

def rodar_experimento():
    criar_pastas()
    entradas = carregar_dados()
    
    if not entradas:
        print("ERRO: Nenhuma lista de entrada encontrada. Execute 01_gerar_entradas.py primeiro.")
        return
    
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Algoritmo", "Tamanho", "Cenario", 
                         "Tempo_Medio_s", "Comparacoes_Medias", "Trocas_Medias"])
    
    print("\nIniciando Experimento de Análise de Algoritmos...")

    chaves_ordenadas = sorted(entradas.keys()) 

    for (tamanho, cenario) in chaves_ordenadas:
        lista_base = entradas[(tamanho, cenario)]
        print(f"\n--- Testando N={tamanho} / Cenário: {cenario.capitalize()} ---")
        
        for nome_algoritmo, func_algoritmo in ALGORITMOS.items():
            tempos, comparacoes, trocas = [], [], []
            
            for rep in range(REPETICOES):
                t, c, s = medir_performance(func_algoritmo, lista_base) 
                tempos.append(t)
                comparacoes.append(c)
                trocas.append(s)
            
            tempo_medio = sum(tempos) / REPETICOES
            comp_media = sum(comparacoes) / REPETICOES
            trocas_media = sum(trocas) / REPETICOES
            
            with open(OUTPUT_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([nome_algoritmo, tamanho, cenario, 
                                 f"{tempo_medio:.6f}", round(comp_media), round(trocas_media)])
            
            print(f"    -> {nome_algoritmo}: Tempo {tempo_medio:.4f}s")
                
    print("\nExperimento concluído. Resultados salvos em:", OUTPUT_FILE)

if __name__ == '__main__':
    rodar_experimento()