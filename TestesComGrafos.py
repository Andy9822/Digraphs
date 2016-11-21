class Fila:
    def __init__(self):
        self.Fila = []
    def Inserir(self, Info):
        self.Fila.append(Info)
    def PopPrimeiroElemento():
        return self.Fila.pop()
    def FilaVazia():
        return len(self.Fila) == 0


class Grafo:
    def __init__(self,listAdjacentes ,Info):
        self.listAdjacentes = listAdjacentes
        self.Info = Info

    """def ComparaComponente2Nodos(NodoRaiz, NodoComparado):
        FilaDeComparacao = Fila()
        ListaDeComparados = []
        FilaDeComparacao.Inserir(NodoRaiz)"""



def main():
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





    pass

if __name__ == '__main__':
    main()



#-------------------------------------------------------------------------------
