from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np

"""An implementation of the adjacency list representation of a graph"""


class AdjacencyMatrix(Graph):

    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i: int, j: int):
        self.adj[i][j] = 1

    def remove_edge(self, i: int, j: int):
        if self.adj[i][j] == 1:
            self.adj[i][j] = 0
            return True
        return False

    def has_edge(self, i: int, j: int) -> bool:
        return self.adj[i][j] == 1

    def out_edges(self, i) -> List:
        out_e = ArrayList.ArrayList()
        for k in range(len(self.adj[i])):
            if self.adj[i][k] == 1:
                out_e.append(k)
        return out_e

    def in_edges(self, j) -> List:
        in_edgs = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.has_edge(k, j):
                in_edgs.append(k)
        return in_edgs

    def bfs(self, r: int):
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n)
        q = ArrayQueue.ArrayQueue()

        traversal.append(r)
        seen[r] = 1
        q.add(r)

        while q.size() > 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for i in range(neighbors.size()):
                neigh = neighbors.get(i)
                if seen[neigh] == 0:
                    traversal.append(neigh)
                    seen[neigh] = 1
                    q.add(neigh)
        return traversal

    def dfs(self, r: int):
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n, dtype=int)
        s = ArrayStack.ArrayStack()

        s.push(r)
        while s.size() > 0:
            current = s.pop()
            print(f"current: {current}\tstack: {s}")
            if seen[current] == 0:
                traversal.append(current)
                seen[current] = 1
                print("\t\tappended to traversal:", traversal)
            neighbors = self.out_edges(current)
            print("\tneighbors:", neighbors)
            for i in reversed(range(neighbors.size())):
                neigh = neighbors.get(i)
                if seen[neigh] == 0:
                    s.push(neigh)
                    print(f"\t\tappended {neigh} to stack:", s)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
    
    def size(self):
        return self.n