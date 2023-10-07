import BinaryHeap
import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
# import BinaryHeap
# import AdjacencyList
import MaxQueue
import time


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, key):
        start_time = time.time()
        idx = self.bookIndices.find(key)

        if idx is not None:
            book = self.bookCatalog.get(idx)
            self.shoppingCart.add(book)
            print("Added title:", book.title)
        else:
            print("Book not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        printed = 0
        n = self.bookCatalog.size()

        for i in range(n):
            book = self.bookCatalog.get(i)
            if infix in book.title:
                print("-" * 25)
                print(book)
                print()
                printed += 1
            if printed == 50:
                break

        print(f"Infix Matches: {printed}")

        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u}\nCompleted in {elapsed_time} seconds")

    def getCartBestSeller(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            best_seller = self.shoppingCart.max().title
            elapsed_time = time.time() - start_time
            print(f"getCartBestSeller returned \n{best_seller} \nCompleted in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix: str):
        if prefix != "":
            b_idx = self.sortedTitleIndices.smallest_geq(prefix).v
            if b_idx is not None:
                book = self.bookCatalog.get(b_idx)
                if len(book.title) >= len(prefix):
                    if book.title[0:len(prefix)] == prefix:
                        self.shoppingCart.add(book)
                        return book.title
        return None

    def bestsellers_with(self, infix, structure, n=0):
        bestsellers = None
        if structure == 1:
            bestsellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            bestsellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")

        if bestsellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()

                iteration = 0
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix in book.title:
                        if structure == 1:
                            bestsellers.add(book.rank, book)
                        else:
                            book.rank = -1 * book.rank
                            bestsellers.add(book)
                        iteration += 1

                        if iteration == n:
                            break

                if structure == 1:
                    books = reversed(bestsellers.in_order())
                    for book in books:
                        print(book.v)
                        print()
                else:
                    while bestsellers.size() > 0:
                        book = bestsellers.remove()
                        book.rank = -1 * book.rank
                        print(book)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with(\"{infix}\", {structure}, {n}) in {elapsed_time} seconds")
