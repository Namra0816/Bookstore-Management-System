"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue
import algorithms as alg


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if not self.adj[i].contains(j):
            self.adj[i].append(j)
            alg.quick_sort(self.adj[i])

    def remove_edge(self, i : int, j : int):
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        in_edg = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.has_edge(k, i):
                in_edg.append(k)
        return in_edg

    def bfs(self, r : int):
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

    def dfs(self, r : int):
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n, dtype=int)
        s = ArrayStack.ArrayStack()

        s.push(r)
        while s.size() > 0:
            current = s.pop()
            if seen[current] == 0:
                traversal.append(current)
                seen[current] = 1
            neighbors = self.out_edges(current)
            for i in reversed(range(neighbors.size())):
                neigh = neighbors.get(i)
                if seen[neigh] == 0:
                    s.push(neigh)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

    def size(self):
        return self.n