from digraph import *
import re

print("Trabalho de Teoria dos Grafos e Análise Combinatória")
print("Alunos: Lucas Hagen, Andy Ruiz e Leonardo Bombardelli\n")
fileName = input("Digite o nome do arquivo a ser lido (com .txt): ")
print("Lendo arquivo '" + fileName + "':")

f = open(fileName, "r")
text = f.read()
f.close()

graph = Digraph().importFromText(text)

print("\nComponentes do Dígrafo: " + str(graph.getSCComponents()).replace("'", ""))

tpSort = graph.topologicalSorting()
if tpSort != None:
    print("Ordenamento Topológico: " + str(tpSort).replace("'", "").replace("[", "").replace("]", ""))
else:
    print("Ordenamento Topológico: grafo é cíclico, portanto, não possui ordenamento topológico!")
