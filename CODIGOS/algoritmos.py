import time

# --- Função de Medição e Execução ---
def medir_performance(algoritmo, arr):
    arr_copy = arr[:] 

    comparacoes = 0
    trocas = 0
    
    start_time = time.perf_counter()
    
    lista_ordenada, comparacoes, trocas = algoritmo(arr_copy)
    
    end_time = time.perf_counter()
    tempo = end_time - start_time
    
    return tempo, comparacoes, trocas

# --- 1. Cocktail Sort ---
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    comparacoes = 0
    trocas = 0
    
    while swapped:
        swapped = False
        
        # Varredura da esquerda para a direita
        for i in range(start, end):
            comparacoes += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocas += 1
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end = end - 1
        
        # Varredura da direita para a esquerda 
        for i in range(end - 1, start - 1, -1):
            comparacoes += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocas += 1
                swapped = True
        
        start = start + 1
        
    return arr, comparacoes, trocas

# --- 2. Bubble Sort ---
def bubble_sort(arr):
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

# --- 3. Selection Sort ---
def selection_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1 
            
    return arr, comparacoes, trocas

# --- 4. Insertion Sort ---
def insertion_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparacoes += 1 
            if key < arr[j]:
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
            else:
                break 
        
        arr[j + 1] = key
        
    return arr, comparacoes, trocas
