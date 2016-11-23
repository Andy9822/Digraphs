import re
import tkinter.filedialog as filedialog
from tkinter import *


class Fila:
    def __init__(self):
        self.Fila = []
    def Inserir(self, Info):
        self.Fila.append(Info)
    def PopPrimeiroElemento():
        return self.Fila.pop()
    def FilaVazia():
        return len(self.Fila) == 0

    """def ComparaComponente2Nodos(NodoRaiz, NodoComparado):
        FilaDeComparacao = Fila()
        ListaDeComparados = []
        FilaDeComparacao.Inserir(NodoRaiz)"""



def funcaoBombardelliNaoLembroQQFazENaoSeiNomear():
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    #Lemos n do documento de teste, e fazemos
    ListaDeGrefos = []
    ListaDeGrefos.append(Grafo([],0))
    ListaDeGrefos.append(Grafo([],1))
    ListaDeGrefos.append(Grafo([],2))
    #Fazemos isso ate n-1

    #Lemos os nodos conectados ao primeiro nodo, e fazemos
    ListaDeGrefos[0].listAdjacentes.append(ListaDeGrefos[1]) #Implementamos isso em um for, por exemplo

    #Repetimos o processo ate n-1
    ListaDeGrefos[1].listAdjacentes.append(ListaDeGrefos[2])
    ListaDeGrefos[1].listAdjacentes.append(ListaDeGrefos[0])

    ListaDeGrefos[2].listAdjacentes.append(ListaDeGrefos[0])









#-------------------------------------------------------------------------------
class Nodo(object):
     def __init__(self, valor, listaAdjacentes):
             self.valor = valor
             self.listaAdjacentes = listaAdjacentes

def readFile():
    window=Tk()
    fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Txt files","*.txt"),("all files","*.*")))
    window.destroy()
    File = open(fileName,'r')
    lista = []
    File.readline()
    vertices = int (File.readline())
    for x in range(vertices):
        linha = File.readline()
        SONUMEROS = re.findall(r'\d+', linha)
        node = SONUMEROS[0]
        SONUMEROS.pop(0)
        lista.append(Nodo(node,SONUMEROS))

        print(node,end=' ')
        print("conecta com", end=' ')
        print(SONUMEROS)
        print('\n')
    File.close()

readFile()
