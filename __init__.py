from digraph import *
import re
from tkinter import *
import tkinter.filedialog as filedialog

print("Trabalho de Teoria dos Grafos e Análise Combinatória")
print("Alunos: Lucas Hagen, Andy Ruiz e Leonardo Bombardelli\n")
window=Tk()
fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select graph file",filetypes = (("Txt files","*.txt"),("all files","*.*")))
window.destroy()
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
