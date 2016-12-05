import copy
import re

"""
    Digraph: Classe de um dígrafo, onde os nodos são salvos por lista de adjacência
    Autores: Lucas Hagen, Andy Ruiz e Leonardo Bombardelli
"""
class Digraph(object):
    nodes = {} # Dicionário com os nodos e seus adjacentes

    """ Inicialização """
    def __init__(self):
        self.nodes = {}

    """
        addNode: Função para adicionar um nodo no dígrafo
        @param node: representação do nodo, pode ser um número ou um caractere
    """
    def addNode(self, node):
        if node not in self.nodes.keys():
            self.nodes[node] = []

    """
        addNode: Função para adicionar nodos no dígrafo
        @param nodes: lista de nodos (um nodo é um número ou um caractere)
    """
    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)

    """
        addEdge: Função que adiciona um arco entre dois nodos.
        @param origin: nodo de origem (número/caractere)
        @param dest: nodo de destino (número/caractere)
    """
    def addEdge(self, origin, dest):
        self.addNodes([origin, dest])
        self.nodes[origin].append(dest)

    """
        addEdges: Função que adiciona arcos do nodo de origem para os nodos dest expecificados.
        @param origin: nodo de origem (número/caractere)
        @param edges: lista de nodos de destino (lista de números/caracteres)
    """
    def addEdges(self, node, edges):
        self.addNodes([node] + edges)
        self.nodes[node] = list(set(self.nodes[node] + edges))

    """
        removeNode: Função que remove o um nodo.
        @param node: nodo a ser removido (número/caractere)
    """
    def removeNode(self, node):
        if node in self.nodes.keys():
            self.nodes.pop(node)
            for n in self.nodes.keys():
                if node in self.nodes[n]:
                    self.nodes[n].remove(node)

    """
        containsNode: Função que verifica um nodo existe no digrafo.
        @param node: nodo a ser pesquisado (número/caractere)

        @return: Boolean
    """
    def containsNode(self, node):
        return node in self.nodes.keys()

    """
        connectedBFS: Função que verifica se dois nodos estão conectados. É utilizado busca em amplitude.
        @param origin: nodo de origem (número/caractere)
        @param dest: nodo de destino (número/caractere)

        @return: Boolean
    """
    def connectedBFS(self, origin, dest):
        nodeQueue = []
        checked = []
        nodeQueue.insert(0, origin)

        while nodeQueue != []:
            temp = nodeQueue.pop()

            if temp not in checked:
                checked.append(temp)
                if dest in self.nodes[temp]:
                    return True
                else:
                    for i in self.nodes[temp]:
                        nodeQueue.insert(0, i)
        return False

    """
        connectedBFS: Função que retorna todos os arcos

        @return: Lista de lista de nodos no seguinte formato: [arco1, arco2, arco3, ...], onde:
            arco1 = [0, 1]
            arco2 = [1, 0]
            arco3 = [nodoOrigem, nodoDestino]
    """
    def getAllEdges(self):
        connections = []
        for node, edges in self.nodes.items():
            for dest in edges:
                if [node, dest] not in connections:
                    connections.append([node, dest])
        return connections

    """
        isCiclic: Função que verifica se o dígrafo é cíclico.

        @return: Boolean
    """
    def isCiclic(self):
        for node in self.nodes.keys():
            nodeQueue = []
            checked = []
            nodeQueue.insert(0, node)

            while nodeQueue:
                temp = nodeQueue.pop()

                if temp not in checked:
                    checked.append(temp)
                    if node in self.nodes[temp]:
                        return True
                    else:
                        for i in self.nodes[temp]:
                            nodeQueue.insert(0, i)
        return False

    """
        reverseDigraph: Função que inverte todos os arcos do dígrafo

        @return: Novo Digraph com os arcos invertidos
    """
    def reverseDigraph(self):
        reverse = Digraph()
        for origin, edges in self.nodes.items():
            for dest in edges:
                reverse.addEdge(dest, origin)
        return reverse

    """
        getSCComponents: Função que informa os componentes de um dígrafo.

        @return: Lista de lista de nodos, ex: [[1, 2, 3], [4, 5], [6]]
    """
    def getSCComponents(self):
        components = []
        visited = []
        stack = []

        for node in self.nodes.keys():
            self.DSFUtil(node, visited, stack)

        rDigraph = self.reverseDigraph()

        visited = []
        while stack:
            temp = stack.pop()
            tempCmp = []
            if temp not in visited:
                rDigraph.DSFUtilReverse(temp, visited, tempCmp)
                components.append(tempCmp)

        return components


    def DSFUtil(self, node, visited, stack):
        if node not in visited:
            visited.append(node)
            for child in self.nodes[node]:
                if child not in visited:
                    self.DSFUtil(child, visited, stack)
            stack.append(node)


    def DSFUtilReverse(self, node, visited, component):
        if node not in visited:
            visited.append(node)
            component.insert(0, node)
            for child in self.nodes[node]:
                if child not in visited:
                    self.DSFUtilReverse(child, visited, component)


    def copyDigraph(self):
        return copy.deepcopy(self)


    def topologicalSorting(self):
        if self.isCiclic():
            return None

        cpy = self.copyDigraph()
        temp = []
        while cpy.nodes:
            temp.append(cpy.popNoParentsNode())
        return temp


    def popNoParentsNode(self):
        if self.isCiclic():
            return None

        for node in self.nodes.keys():
            if not self.nodeHasParents(node):
                self.removeNode(node)
                return node


    def nodeHasParents(self, node):
        for edges in self.nodes.values():
            if node in edges:
                return True
        return False

    def importFromText(self, str):
        for nodeStr in re.findall("([(][0-9 \n]+[)])", str):
            nodeData = re.findall("[0-9a-zA-Z]+", nodeStr)
            self.addEdges(nodeData[0], nodeData[1:])
        return self
