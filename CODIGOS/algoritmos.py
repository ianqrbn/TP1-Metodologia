import time

# --- Função de Medição e Execução ---
def medir_performance(algoritmo, arr):
    """Executa o algoritmo, mede o tempo, comparações e trocas."""
    arr_copy = arr[:] # Cópia para não alterar o original
    
    # Inicializa métricas
    comparacoes = 0
    trocas = 0
    
    start_time = time.perf_counter()
    
    # Executa o algoritmo, que retorna a lista ordenada e as métricas
    lista_ordenada, comparacoes, trocas = algoritmo(arr_copy)
    
    end_time = time.perf_counter()
    tempo = end_time - start_time
    
    return tempo, comparacoes, trocas

# --- 1. Cocktail Sort (Seu Algoritmo) ---
def cocktail_sort(arr):
    """Implementação do Cocktail Sort, contando comparações e trocas."""
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    comparacoes = 0
    trocas = 0
    
    while swapped:
        swapped = False
        
        # 1. Varredura da esquerda para a direita (Bubble Sort padrão)
        for i in range(start, end):
            comparacoes += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocas += 1
                swapped = True
        
        # Se nenhuma troca ocorreu, a lista está ordenada
        if not swapped:
            break
        
        swapped = False
        end = end - 1
        
        # 2. Varredura da direita para a esquerda (Shaker)
        for i in range(end - 1, start - 1, -1):
            comparacoes += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocas += 1
                swapped = True
        
        start = start + 1
        
    return arr, comparacoes, trocas

# --- 2. Bubble Sort (Baseline) ---
def bubble_sort(arr):
    """Implementação do Bubble Sort, contando comparações e trocas."""
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                swapped = True
        if not swapped:
            break
            
    return arr, comparacoes, trocas

# --- 3. Selection Sort (Baseline) ---
def selection_sort(arr):
    """Implementação do Selection Sort, contando comparações e trocas."""
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Realiza a troca (swap) fora do loop interno
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1 # Conta apenas a troca final
            
    return arr, comparacoes, trocas

# --- 4. Insertion Sort (Baseline) ---
def insertion_sort(arr):
    """Implementação do Insertion Sort, contando comparações e trocas."""
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparacoes += 1 # Comparação dentro do while
            if key < arr[j]:
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
            else:
                break # Sai assim que encontra a posição correta
        
        arr[j + 1] = key
        
    return arr, comparacoes, trocas

if __name__ == '__main__':
    # Exemplo rápido de teste
    lista = [5, 1, 4, 2, 8]
    t, c, s = medir_performance(cocktail_sort, lista)
    print(f"Cocktail Sort - Tempo: {t:.6f}s, Comparações: {c}, Trocas: {s}")