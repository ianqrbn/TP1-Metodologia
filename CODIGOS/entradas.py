import random
import json
import os

# --- Configurações de Geração ---
TAMANHOS = [100, 500, 1000, 5000, 10000, 20000] # Adicione tamanhos maiores aqui, se necessário (ex: 50000)
CENARIOS = ["aleatorio", "ordenado", "reverso"]
PASTA_DADOS = "DADOS"

def criar_pastas():
    """Cria a pasta 'DADOS' se ela não existir."""
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)
        print(f"Pasta '{PASTA_DADOS}/' criada.")

def gerar_lista(tamanho, cenario):
    """Gera uma lista com base no tamanho e cenário."""
    # Lista base de números aleatórios
    lista = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    if cenario == "ordenado":
        return sorted(lista)
    elif cenario == "reverso":
        return sorted(lista, reverse=True)
    else: # "aleatorio"
        return lista

def salvar_entrada(lista, tamanho, cenario):
    """Salva a lista em um arquivo JSON na pasta 'dados'."""
    nome_arquivo = f"{PASTA_DADOS}/{cenario}_N{tamanho}.json"
    
    with open(nome_arquivo, 'w') as f:
        # Usamos dump para salvar a lista no formato JSON
        json.dump(lista, f)
    
    print(f"  -> Gerado e salvo: {nome_arquivo}")

def main_geracao():
    criar_pastas()
    print("Iniciando a Geração das Entradas para o Experimento...")
    
    for tamanho in TAMANHOS:
        print(f"\nGerando listas de Tamanho N={tamanho}:")
        for cenario in CENARIOS:
            lista = gerar_lista(tamanho, cenario)
            salvar_entrada(lista, tamanho, cenario)
            
    print("\nGeração de Entradas concluída. Dados armazenados em 'dados/'.")

if __name__ == '__main__':
    main_geracao()