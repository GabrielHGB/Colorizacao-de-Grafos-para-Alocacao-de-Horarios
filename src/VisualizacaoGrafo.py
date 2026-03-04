import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from termcolor import colored
from colorama import Fore, Style
import time
CORES_TERMINAL = ["yellow", "cyan", "green", "magenta", "red", "blue", "white"]

# Leitura do arquivo
def carregar_dataset(caminho_csv):
    df = pd.read_csv(caminho_csv)
    arestas = list(zip(df['Disciplina1'], df['Disciplina2']))
    return arestas

# Imprimir o resultado com cores, para melhor visualização
def imprimir_resultados(coloracao):
    print("=== Resultado da Coloração Agrupada ===\n")

    grupos = {}
    for disciplina, cor in coloracao.items():
        grupos.setdefault(cor, []).append(disciplina)

    for cor, disciplinas in sorted(grupos.items()):
        nome_cor = CORES_TERMINAL[cor % len(CORES_TERMINAL)]
        titulo = colored(f"Coloração = {nome_cor.upper()}, Horário = {cor}:", nome_cor, attrs=["bold"])
        print(titulo)

        for d in sorted(disciplinas):
            print(colored(f"  - {d}", nome_cor))
        print()

# Gerar o grafo para visualizar
def gerar_visualizacao(G, coloracao):
    """Gera o grafo colorido com as mesmas cores mostradas no terminal."""
    print(f"\n{Fore.MAGENTA}Gerando visualização do grafo...{Style.RESET_ALL}")

    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42)
    cores = [CORES_TERMINAL[coloracao[n] % len(CORES_TERMINAL)] for n in G.nodes()]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=cores,
        node_size=900,
        font_color='black',
        font_weight='bold'
    )

    plt.title("Grafo de Conflitos (Coloração por Horário)", fontsize=14, fontweight='bold')
    plt.savefig("grafo_colorido.png")
    print("Grafo salvo como 'grafo_colorido.png' na pasta atual.")

# Pequena animação de carregamento
def animacao_carregamento(texto="Processando", duracao=2.5, pontos=5):
    """Exibe uma pequena animação de carregamento no terminal."""
    print(f"{Fore.CYAN}{texto}", end="", flush=True)
    for _ in range(pontos):
        print(f"{Fore.CYAN}.", end="", flush=True)
        time.sleep(duracao / pontos)
    print(f"{Style.RESET_ALL}\n")
