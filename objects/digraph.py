class Digraph(object):
    nodes = {}

    def __init__(self):
        self.nodes = {}

    def newNode(self, value):
        if value not in self.nodes.keys():
            self.nodes[value] = []

    def newCompleteNode(self, value, edges):
        if value in self.nodes.keys():
            raise AttributeError
        else:
            self.nodes[value] = edges

    def newEdge(self, origin, to):
        if origin not in self.nodes.keys():
            raise AttributeError
        else:
            self.nodes[origin].append(to)

    def containsNode(self, value):
        return value in self.nodes.keys()

    def connectedBFS(self, origin, to):
        nodeQueue = []
        checked = []
        nodeQueue.insert(0, origin)

        while nodeQueue != []:
            temp = nodeQueue.pop()

            if temp not in checked:
                checked.append(temp)
                if to in self.nodes[temp]:
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

            while nodeQueue != []:
                temp = nodeQueue.pop()

                if temp not in checked:
                    checked.append(temp)
                    if node in self.nodes[temp]:
                        return True
                    else:
                        for i in self.nodes[temp]:
                            nodeQueue.insert(0, i)
        return False

    """def getComponent(self, startNode):
        if not self.containsNode(startNode):
            return []
        else:
            return self.getRoutes(startNoe)

    def getRoutes(self, node, dest):




    return startNode"""
