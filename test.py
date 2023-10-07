from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object, value: object) -> object:
        h = self._hash(key)
        for i in range(self.t[h].size()):
            if self.t[h].get(i).key == key:
                return self.t[h].get(i).value
        return None
        # h = self._hash(key)
        # for node in self.t[h]:
        #     if node.key == key:
        #         return node.value
        # return None

    def add(self, key: object, value: object):
        # if self.find(key) != None:
        #     return False
        # if n == len(self.t):
        #     self.resize()
        # h = hash(key)
        # item = self.Node(key, value)
        # self.t[h].add(0, item)
        # n += 1
        # return True
        h = self._hash(key)
        for node in self.t[h]:
            if node.key == key:
                return False
        self.t[h].append(self.Node(key, value))
        self.n += 1
        if self.n > len(self.t):
            self.resize()
        return True

    def remove(self, key: int) -> object:
        # h = self._hash(key)
        # for i in range(0, self.t[h].size(), 1):
        #     if self.t[h].get(i).key == key:
        #         self.t[h].remove(i)
        #         self.n -= 1
        #         if len(self.t) > (3 * self.n):
        #             self.resize()
        #         return True    
        # return None
        h = self._hash(key)
        for i in range(len(self.t[h])-1):
            node = self.t[h][i]
            if node.key == key:
                val = node.value
                self.t[h].remove(node)
                self.n -= 1
                if len(self.t) > (3 * self.n):
                    self.resize()
            return val
        return None

    def resize(self):

        # if self.n == len(t):
        #     d += 1
        # else:
        #     d -= 1
        # temp = [[] for i in range(2**d)]
        # for j in range(len(self.t)):
        #     for i in range(self.t[j].size()):
        #         bin = hash(self.t[j].get(i).key) % len(temp)
        #         temp[bin].append(self.t[j].get(i))
        # t = temp
        self.d += 1
        old_t = self.t
        self.t = self.alloc_table(2 ** self.d)
        for lst in old_t:
            for node in lst:
                h = self._hash(node.key)
                self.t[h].append(node)

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
