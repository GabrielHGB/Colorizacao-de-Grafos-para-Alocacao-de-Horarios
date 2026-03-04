from colorama import Fore, Style, init
import time
import os
import networkx as nx

# Importa todas as funções para auxiliar na visualização do nosso programa
from VisualizacaoGrafo import (
    carregar_dataset,
    imprimir_resultados,
    gerar_visualizacao,
    animacao_carregamento,
)

init(autoreset=True)

def main():
    print(f"{Style.BRIGHT}{Fore.CYAN}=== Sistema de Alocação de Horários (Coloração de Grafos) ==={Style.RESET_ALL}\n")

    nome_arquivo = input(f"{Fore.YELLOW}Digite o nome do arquivo CSV (ex: pequeno.csv, medio.csv, grande.csv): {Style.RESET_ALL}").strip()
    caminho_csv = f"datasets_coloring/{nome_arquivo}"

    if not os.path.exists(caminho_csv):
        print(f"{Fore.RED}❌ Erro: o arquivo '{caminho_csv}' não foi encontrado.{Style.RESET_ALL}")
        return

    # Leitura de todas as arestas 
    arestas = carregar_dataset(caminho_csv)
    print(f"Foram lidas {len(arestas)} relações de conflito.\n")

    # Chamada da função Graph, para montar o grafo
    G = nx.Graph()
    G.add_edges_from(arestas)
    print(f"O grafo possui {G.number_of_nodes()} disciplinas e {G.number_of_edges()} conflitos.\n")

    # Usamos o algoritmo DSATUR, para aplicar a coloração.
    print(f"Iniciando coloração com o algoritmo DSATUR")
    animacao_carregamento("Processando grafo", duracao=3.0)
    inicio = time.time()
    coloracao = nx.coloring.greedy_color(G, strategy="DSATUR")
    fim = time.time()
    tempo_execucao = fim - inicio

    # Aplicação de cores para uma melhor visualização do grafo
    num_cores = len(set(coloracao.values()))
    print(f"{Fore.GREEN}✅ Coloração concluída em {tempo_execucao:.5f} segundos.")
    print(f"Número mínimo de horários (cores): {num_cores}\n{Style.RESET_ALL}")

    # Resultado
    imprimir_resultados(coloracao)

    # Visualizar o Grafo
    ver_grafo = input(f"{Fore.CYAN}Deseja visualizar o grafo colorido? (s/n): {Style.RESET_ALL}").strip().lower()
    if ver_grafo == 's':
        gerar_visualizacao(G, coloracao)


if __name__ == "__main__":
    main()
