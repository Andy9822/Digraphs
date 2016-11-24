from digraph import *


nodeTeste = Digraph()

nodeTeste.addEdge('A', 'B')
nodeTeste.addEdge('B', 'C')
nodeTeste.addEdge('B', 'D')
nodeTeste.addEdge('C', 'A')
nodeTeste.addEdge('D', 'E')
nodeTeste.addEdge('E', 'F')
nodeTeste.addEdge('F', 'D')
nodeTeste.addEdge('G', 'F')
nodeTeste.addEdge('G', 'H')
nodeTeste.addEdge('H', 'I')
nodeTeste.addEdge('I', 'J')
nodeTeste.addEdge('J', 'G')
nodeTeste.addEdge('J', 'K')



print("Edges: " + str(nodeTeste.getAllEdges()))
print("Reverse Edges: " + str(nodeTeste.reverseDigraph().getAllEdges()) + "\n\n")
print("Components: " + str(nodeTeste.getSCComponents()))
