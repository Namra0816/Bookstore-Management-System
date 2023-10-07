from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        new_node = self.Node(key, value)
        parent = self._find_last(key)
        return self._add_child(parent, new_node)

    def find(self, key: object) -> object:
        node = self._find_eq(key)
        if node == None:
            return None
        return node.v

    def remove(self, key: object):
        u = self._find_eq(key)
        if u == None:
            raise ValueError
        value = u.v
        self._remove_node(u)
        return value
        

    def _find_eq(self, key: object) -> BinaryTree.Node:
        current = self.r
        while current is not None:
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        current = self.r
        parent = None
        while current != None:
            parent = current
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return parent

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        if p is None:
            self.r = u
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True



    def _splice(self, u: BinaryTree.Node):
        if u.left is not None:
            child = u.left
        else:
            child = u.right
        if u == self.r:
            self.r = child
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = child
            else:
                p.right = child
        if child is not None:
            child.parent = p
        self.n += 1


    def _remove_node(self, u: BinaryTree.Node):
        if u.left == None or u.right == None:
            self._splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.k = w.k
            u.v = w.v
            self._splice(w)

    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    def smallest_geq(self, key: object) -> object:
        """
        returns the node with the key that either matches the given key,
        or if such does not exist, the node with the smallest key that is larger
        than the given key.
        """
        current = self.r
        smallest = None
        while current is not None:
            if key < current.k:
                smallest = current
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        if smallest is None:
            return None
        return smallest

    def largest_leq(self, key):
        """
        returns the node with the key that either matches the given key,
        or if such key does not exist, the node with the largest key that is smaller
        than the given key
        """
        current = self.r
        largest = None
        while current is not None:
            if current.k < key:
                largest = current
                current = current.right
            elif current.k > key:
                current = current.left
            else:
                return current
        return largest

    def next_smallest_key(self, key):
        nodes = self.in_order()
        i = 0
        while nodes[i].k < key:
            i += 1
        if i > 0:
            return nodes[i - 1].k
        else:
            return None