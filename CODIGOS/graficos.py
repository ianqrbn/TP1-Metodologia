import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# --- 1. Carregar os Dados ---
# Os dados CSV fornecidos pelo usuário são lidos para um DataFrame do pandas.
# O `io.StringIO` permite tratar o texto como se fosse um arquivo.
csv_data = """Algoritmo,Tamanho,Cenario,Tempo_Medio_s,Comparacoes_Medias,Trocas_Medias
Cocktail Sort (Proposto),100,aleatorio,0.000490,4170,2565
Insertion Sort,100,aleatorio,0.000333,2656,2565
Selection Sort,100,aleatorio,0.000322,4950,91
Bubble Sort,100,aleatorio,0.000545,4929,2565
Cocktail Sort (Proposto),100,ordenado,0.000007,99,0
Insertion Sort,100,ordenado,0.000012,99,0
Selection Sort,100,ordenado,0.000273,4950,0
Bubble Sort,100,ordenado,0.000012,99,0
Cocktail Sort (Proposto),100,reverso,0.000745,4950,4950
Insertion Sort,100,reverso,0.000688,4950,4950
Selection Sort,100,reverso,0.000363,4950,50
Bubble Sort,100,reverso,0.000790,4950,4950
Cocktail Sort (Proposto),500,aleatorio,0.012888,93375,63448
Insertion Sort,500,aleatorio,0.008084,63936,63448
Selection Sort,500,aleatorio,0.007353,124750,494
Bubble Sort,500,aleatorio,0.014226,124222,63448
Cocktail Sort (Proposto),500,ordenado,0.000033,499,0
Insertion Sort,500,ordenado,0.000062,499,0
Selection Sort,500,ordenado,0.008020,124750,0
Bubble Sort,500,ordenado,0.000034,499,0
Cocktail Sort (Proposto),500,reverso,0.020531,124750,124750
Insertion Sort,500,reverso,0.015524,124750,124750
Selection Sort,500,reverso,0.007545,124750,250
Bubble Sort,500,reverso,0.019411,124750,124750
Cocktail Sort (Proposto),1000,aleatorio,0.053207,367659,244631
Insertion Sort,1000,aleatorio,0.033038,245624,244631
Selection Sort,1000,aleatorio,0.030548,499500,991
Bubble Sort,1000,aleatorio,0.060243,498324,244631
Cocktail Sort (Proposto),1000,ordenado,0.000069,999,0
Insertion Sort,1000,ordenado,0.000127,999,0
Selection Sort,1000,ordenado,0.029576,499500,0
Bubble Sort,1000,ordenado,0.000068,999,0
Cocktail Sort (Proposto),1000,reverso,0.090933,499500,499499
Insertion Sort,1000,reverso,0.065634,499500,499499
Selection Sort,1000,reverso,0.029685,499500,501
Bubble Sort,1000,reverso,0.083373,499500,499499
Cocktail Sort (Proposto),5000,aleatorio,1.410529,9445815,6297985
Insertion Sort,5000,aleatorio,0.873008,6302970,6297985
Selection Sort,5000,aleatorio,0.719297,12497500,4994
Bubble Sort,5000,aleatorio,1.611980,12494574,6297985
Cocktail Sort (Proposto),5000,ordenado,0.000353,4999,0
Insertion Sort,5000,ordenado,0.000692,4999,0
Selection Sort,5000,ordenado,0.722828,12497500,0
Bubble Sort,5000,ordenado,0.000353,4999,0
Cocktail Sort (Proposto),5000,reverso,2.266670,12497500,12497488
Insertion Sort,5000,reverso,1.737666,12497500,12497488
Selection Sort,5000,reverso,0.732336,12497500,2506
Bubble Sort,5000,reverso,2.247770,12497500,12497488
Cocktail Sort (Proposto),10000,aleatorio,5.583006,37377224,24872100
Insertion Sort,10000,aleatorio,3.417399,24882091,24872100
Selection Sort,10000,aleatorio,2.861195,49995000,9993
Bubble Sort,10000,aleatorio,6.443298,49987497,24872100
Cocktail Sort (Proposto),10000,ordenado,0.000705,9999,0
Insertion Sort,10000,ordenado,0.001390,9999,0
Selection Sort,10000,ordenado,2.925317,49995000,0
Bubble Sort,10000,ordenado,0.000704,9999,0
Cocktail Sort (Proposto),10000,reverso,9.079157,49995000,49994959
Insertion Sort,10000,reverso,6.990385,49995000,49994959
Selection Sort,10000,reverso,2.924070,49995000,5020
Bubble Sort,10000,reverso,9.091638,49995000,49994959
Cocktail Sort (Proposto),20000,aleatorio,22.258861,150184810,99977537
Insertion Sort,20000,aleatorio,13.738241,99997530,99977537
Selection Sort,20000,aleatorio,11.532322,199990000,19987
Bubble Sort,20000,aleatorio,25.925880,199968885,99977537
Cocktail Sort (Proposto),20000,ordenado,0.001425,19999,0
Insertion Sort,20000,ordenado,0.002626,19999,0
Selection Sort,20000,ordenado,11.631698,199990000,0
Bubble Sort,20000,ordenado,0.001441,19999,0
Cocktail Sort (Proposto),20000,reverso,36.053609,199990000,199989812
Insertion Sort,20000,reverso,28.031384,199989997,199989812
Selection Sort,20000,reverso,11.779719,199990000,10087
Bubble Sort,20000,reverso,36.148068,199990000,199989812
"""

df = pd.read_csv(io.StringIO(csv_data))

# --- 2. Configurações de Estilo dos Gráficos ---
# Define um estilo visual mais agradável para os gráficos.
sns.set_theme(style="whitegrid", palette="deep")
cenarios = ['aleatorio', 'ordenado', 'reverso']
metricas = {
    'Tempo_Medio_s': 'Tempo Médio (s)',
    'Comparacoes_Medias': 'Comparações Médias',
    'Trocas_Medias': 'Trocas Médias'
}

# --- 3. Geração dos Gráficos ---
# Itera sobre cada métrica para criar uma figura com 3 subplots (um para cada cenário).
for metrica_col, metrica_titulo in metricas.items():

    # Cria uma figura com 3 subplots organizados em 1 linha e 3 colunas.
    fig, axes = plt.subplots(1, 3, figsize=(20, 6), sharey=False)
    fig.suptitle(f'Análise de Desempenho por Métrica: {metrica_titulo}', fontsize=18, weight='bold')

    # Itera sobre os cenários para popular cada subplot.
    for i, cenario in enumerate(cenarios):
        ax = axes[i]
        df_cenario = df[df['Cenario'] == cenario]

        # Plota os dados usando seaborn.
        sns.lineplot(
            data=df_cenario,
            x='Tamanho',
            y=metrica_col,
            hue='Algoritmo',
            style='Algoritmo',
            markers=True,
            dashes=False,
            ax=ax
        )

        # Configurações específicas para cada subplot.
        ax.set_title(f'Cenário: {cenario.capitalize()}', fontsize=14)
        ax.set_xlabel('Tamanho da Entrada (n)', fontsize=12)
        ax.set_ylabel(metrica_titulo, fontsize=12)
        ax.legend(title='Algoritmo')

        # A escala logarítmica ajuda a visualizar melhor grandes variações de valores,
        # exceto para o cenário ordenado que tem valores muito baixos ou zero.
        #if cenario != 'ordenado':
        #    ax.set_yscale('log')

        # Melhora a legibilidade dos eixos.
        ax.tick_params(axis='x', rotation=45)
        ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # Ajusta o layout para evitar sobreposição e salva a figura.
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    nome_arquivo = f'grafico_{metrica_col}.png'
    plt.savefig(nome_arquivo, dpi=300)
    print(f'Gráfico salvo como: {nome_arquivo}')

# Exibe os gráficos (opcional, pode ser removido se só quiser salvar os arquivos)
plt.show()
