from digraph import *
import re

print("Trabalho de Teoria dos Grafos e Análise Combinatória")
print("Alunos: Lucas Hagen, Andy Ruiz e Leonardo Bombardelli\n")
fileName = input("Digite o nome do arquivo a ser lido: ")

try:
    f = open(fileName, "r") # Abre o arquivo
    print("Lendo arquivo '" + fileName + "':")
    text = f.read() # Carrega o buffer do arquivo
    f.close()

    graph = Digraph().importFromText(text) # Carrega o grafo a partir do buffer do arquivo

    print("\nComponentes do Dígrafo: " + str(graph.getSCComponents()).replace("'", "")) # Exibe os componentes

    tpSort = graph.topologicalSorting() # Carrega o ordenamento Topológico
    if tpSort != None:
        print("Ordenamento Topológico: " + str(tpSort).replace("'", "").replace("[", "").replace("]", ""))
    else:
        print("Ordenamento Topológico: grafo é cíclico, portanto, não possui ordenamento topológico!")
except Exception:
    print("Erro ao abrir arquivo!")
