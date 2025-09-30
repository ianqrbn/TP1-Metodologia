import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

df = pd.read_csv("./RESULTADOS/resultados_experimentais.csv")

sns.set_theme(style="whitegrid", palette="deep")
cenarios = ['aleatorio', 'ordenado', 'reverso']
metricas = {
    'Tempo_Medio_s': 'Tempo Médio (s)',
    'Comparacoes_Medias': 'Comparações Médias',
    'Trocas_Medias': 'Trocas Médias'
}

for metrica_col, metrica_titulo in metricas.items():

    fig, axes = plt.subplots(1, 3, figsize=(20, 6), sharey=False)
    fig.suptitle(f'Análise de Desempenho por Métrica: {metrica_titulo}', fontsize=18, weight='bold')

    for i, cenario in enumerate(cenarios):
        ax = axes[i]
        df_cenario = df[df['Cenario'] == cenario]

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

        ax.set_title(f'Cenário: {cenario.capitalize()}', fontsize=14)
        ax.set_xlabel('Tamanho da Entrada (n)', fontsize=12)
        ax.set_ylabel(metrica_titulo, fontsize=12)
        ax.legend(title='Algoritmo')
        ax.tick_params(axis='x', rotation=45)
        ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    nome_arquivo = f'./RESULTADOS/grafico_{metrica_col}.png'
    plt.savefig(nome_arquivo, dpi=300)
    print(f'Gráfico salvo como: {nome_arquivo}')

plt.show()
