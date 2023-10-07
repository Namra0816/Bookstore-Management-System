import numpy as np
from Interfaces import Stack
from Interfaces import List


class ArrayStack(Stack, List):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)
    
    def resize(self):
        b = self.new_array(max(1, 2*self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b
        pass 

    def get(self, i : int) -> object:
        if i < 0 or i > self.n-1:
            raise IndexError()
        return self.a[i]
        
    
    def set(self, i : int, x : object) -> object:
        if i < 0 or i > self.n-1:
            raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y
    
    def add(self, i: int, x : object) :
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self.resize()
        for j in range(self.n, i, -1):
            self.a[j] = self.a[j-1]
        self.a[i] = x
        self.n += 1 

    def remove(self, i : int) -> object :
        if i < 0 or i > self.n-1:
            raise IndexError()
        x = self.a[i]
        for j in range(i, self.n-1):
            self.a[j] = self.a[j+1]
        self.n -= 1
        if len(self.a) >= 3*self.n:
            self.resize()
        return x

    def push(self, x : object) :
        self.add(self.n, x)
    
    def pop(self) -> object :
        return self.remove(self.n-1)

    def size(self) :
        
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
        




