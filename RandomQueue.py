import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
    
    #remove a random element
    #You can call the method of the parent class using super(). e.g.
    #super().remove()
    
        if self.n == 0:
            raise IndexError("Queue is empty")
        index = random.randint(0, self.n-1)
        x = self.a[(index + self.j) % len(self.a)]
        self.a[(index + self.j) % len(self.a)] = None
        for i in range(index, self.n-1):
            self.a[(i + self.j) % len(self.a)] = self.a[(i + self.j + 1) % len(self.a)]
        self.a[(self.j + self.n - 1) % len(self.a)] = None
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()
        return x



