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
def oneComponente(listaGrafo):
    boolean = True
    for i in listaGrafo:
        for j in listaGrafo:
            boolean = boolean and connectedBFS(i.valor,j.valor,listaGrafo)
    return boolean

def achaNodo(valor,listaGrafo):
    for x in listaGrafo:
        if x.valor == valor:
            startingNode = x
            return startingNode
    return 'error'

def connectedBFS(origin, destiny,listaGrafo):
    nodeQueue = []
    checked = []
    nodeQueue.insert(0, origin)

    while nodeQueue != []:
        tempValor = nodeQueue.pop()
        nodoAtual = achaNodo(tempValor,listaGrafo)

        if nodoAtual != 'error' and nodoAtual.valor not in checked:
            checked.append(nodoAtual.valor)
            if destiny in nodoAtual.listaAdjacentes:
                return True
            else:
                for i in nodoAtual.listaAdjacentes:
                    nodeQueue.insert(0, i)
    return False

def printConecions(listaGrafo):
    for x in listaGrafo:
        print(x.valor,end=' ')
        print("conecta com", end=' ')
        print(x.listaAdjacentes)
    print("")

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
        SONUMEROS = [int(x) for x in SONUMEROS]
        node = SONUMEROS[0]
        SONUMEROS.pop(0)
        lista.append(Nodo(node,SONUMEROS))

    File.close()
    return lista



listaGrafo = readFile()
printConecions(listaGrafo)
if oneComponente(listaGrafo):
    print("O grafo so possui 1 componente")
else:
    print("O grafico possui mais de 1 componente")
