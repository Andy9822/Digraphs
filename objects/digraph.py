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
