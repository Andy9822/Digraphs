class Digraph:
    def __init__():
        self.nodes = {}

    def __str__():
        return "Digraph"

    def newNode(value):
        if value not in self.nodes.keys:
            self.nodes[value] = []

    def newNode(value, edges):
        if value in self.nodes.keys:
            raise AttributeError
        else:
            self.nodes[value] = edges

    def newEdge(origin, to):
        if origin not in self.nodes.keys:
            raise AttributeError
        else:
            self.nodes[origin].append(to)

    def containsNode(value):
        return value in self.nodes.keys

    def connectedBFS(origin, to):
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
