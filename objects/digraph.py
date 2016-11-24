import copy

class Digraph(object):
    nodes = {}


    def __init__(self):
        self.nodes = {}


    def addNode(self, node):
        if node not in self.nodes.keys():
            self.nodes[node] = []

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)


    def addEdge(self, origin, dest):
        self.addNodes([origin, dest])
        self.nodes[origin].append(dest)


    def addEdges(self, node, edges):
        self.addNodes([node] + edges)
        self.nodes[node] = list(set(self.nodes[node] + edges))


    def removeNode(self, node):
        if node in self.nodes.keys():
            self.nodes.pop(node)
            for n in self.nodes.keys():
                if node in self.nodes[n]:
                    self.nodes[n].remove(node)


    def containsNode(self, node):
        return node in self.nodes.keys()


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


    def getAllEdges(self):
        connections = []
        for node, edges in self.nodes.items():
            for dest in edges:
                if [node, dest] not in connections:
                    connections.append([node, dest])
        return connections


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


    def reverseDigraph(self):
        reverse = Digraph()
        for origin, edges in self.nodes.items():
            for dest in edges:
                reverse.addEdge(dest, origin)
        return reverse


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
