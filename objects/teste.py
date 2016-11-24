from digraph import *

cmp = Digraph()

cmp.addEdge('A', 'B')
cmp.addEdge('B', 'C')
cmp.addEdge('B', 'D')
cmp.addEdge('C', 'A')
cmp.addEdge('D', 'E')
cmp.addEdge('E', 'F')
cmp.addEdge('F', 'D')
cmp.addEdge('G', 'F')
cmp.addEdge('G', 'H')
cmp.addEdge('H', 'I')
cmp.addEdge('I', 'J')
cmp.addEdge('J', 'G')
cmp.addEdge('J', 'K')

print("Components: " + str(cmp.getSCComponents()))

tSort = Digraph()

tSort.addEdges(1, [2, 3, 4])
tSort.addEdges(2, [4, 5])
tSort.addEdges(3, [6])
tSort.addEdges(4, [3, 6, 7])
tSort.addEdges(5, [4, 7])
tSort.addEdges(6, [])
tSort.addEdges(7, [6])

print("Topological Sorting: " + str(tSort.topologicalSorting()))
