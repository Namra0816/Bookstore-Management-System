from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n  :
            raise Exception()
        if i < (self.n)/2 :          
            self.p = self.dummy.next
            for j in range(i):
                self.p = self.p.next 
        else:
            self.p = self.dummy
            for k in range(self.n - i):
                self.p = self.p.prev 
        return self.p

    def get(self, i) -> object:
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object):
        if i<0 or i > self.n:
            raise Exception()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next 
        w.next.prev = w.prev
        self.n -= 1

    
    def remove(self, i: int) -> object:
        if i < 0 or i > self.n:
            raise IndexError()
        # if i < self.value or i > self.value + self.n:
        #     raise IndexError()
        w = self.get_node(i)
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x
       

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    
    def reverse(self):
        if self.n <= 1:
            return #self.n
        current_node = self.dummy.next
        while current_node is not self.dummy:
            temp = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp
            current_node = temp
        temp = self.dummy.next
        self.dummy.next = self.dummy.prev
        self.dummy.prev = temp

    def isPalindrome(self) -> bool:
        if self.n == 0:
            return True
        u = self.dummy.next
        v = self.dummy.prev
        while u != v:
            if u.x != v.x:
                return False
            u = u.next
            v = v.prev
        return True

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
