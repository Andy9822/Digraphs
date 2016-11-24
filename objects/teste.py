from digraph import *


nodeTeste = Digraph()
nodeTeste.newNode(0)
nodeTeste.newNode(1)
nodeTeste.newNode(2)
nodeTeste.newNode(3)
nodeTeste.newNode(4)
nodeTeste.newNode(5)

nodeTeste.newEdge(0, 1)
nodeTeste.newEdge(1, 4)
nodeTeste.newEdge(4, 3)
nodeTeste.newEdge(4, 5)
nodeTeste.newEdge(3, 1)
nodeTeste.newEdge(5, 2)
nodeTeste.newEdge(2, 5)


print(nodeTeste.isCiclic())

print("Fim")
