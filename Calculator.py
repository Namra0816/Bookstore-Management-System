import numpy as np
import SLLStack
import ArrayStack
import ChainedHashTable
import DLList
import operator
import re
 
import BinaryTree
 
 
def _make_tokens(expr: str) -> list:
    variables = [x for x in re.split('\W+', expr) if x.isalnum()]
    ee = re.split('\w+', expr)
    tokens = []
    while len(variables) > 0 and len(ee) > 0:
        if len(ee[0]) < 2:
            tokens.append(ee[0])
        else:
            for c in ee[0]:
                tokens.append(c)
        del ee[0]
        tokens.append(variables[0])
        del variables[0]
 
    while len(ee) > 0:
        if len(ee[0]) < 2:
            tokens.append(ee[0])
        else:
            for c in ee[0]:
                tokens.append(c)
        del ee[0]
    return tokens
 
 
class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
 
    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)
 
    def matched_expression(self, s: str) -> bool:
        parens = ArrayStack.ArrayStack()
        for c in s:
            if c == "(":
                parens.push(c)
            if c == ")":
                if parens.size() > 0:
                    parens.pop()
                else:
                    return False
        return parens.size() == 0
 
    def print_expression(self, expr: str):
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]
        e = re.split('\w+', expr)
        for i in range(len(variables)):
            var = variables[i]
            val = self.dict.find(var)
            if val is not None:
                variables[i] = str(val)
        exp2 = ""
        while len(variables) > 0 and len(e) > 0:
            exp2 += e[0] + variables[0]
            del variables[0]
            del e[0]
 
        while len(e) > 0:
            exp2 += e[0]
            del e[0]
        print(exp2)
        return exp2
 
    def evaluate(self, expr: str):
        parse_tree = self._build_parse_tree(expr)
        return self._evaluate(parse_tree.r)
 
    def _evaluate(self, u: BinaryTree.BinaryTree.Node):
        fn = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
 
        if u.left is not None and u.right is not None:  # this is an operator
            return fn[u.v](self._evaluate(u.left), self._evaluate(u.right))
        elif u.left is None and u.right is None:  # this must be a variable
            if u.k is None:
                raise ValueError(f"Missing operand after {u.parent.k}.")
            elif u.v is not None:
                return u.v
            else:
                raise ValueError(f"Missing value for variable '{u.k}'")
        else:
            raise ValueError(f"Missing an operand and/or operator before {u.left.v}.")
 
    def _build_parse_tree(self, expr: str) -> str:
        if not self.matched_expression(expr):
            raise ValueError("Expression contains unmatched parenthesis.")
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node()
        # print(type(t.r))
        current = t.r
        # print("Before loop current", current)
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]
        tokens = _make_tokens(expr)
        # print(tokens)
        for token in tokens:
            # print("Current token:", token)
            if token == '(':
                # print("\tCurrent node:", current)
                current.insert_left(BinaryTree.BinaryTree.Node())
                current = current.left
                # print("\tAdded a left child. Current node is now left child:", current)
            elif token in ['+', '-', '*', '/']:
                # print("\tCurrent node (before val):", current)
                current.set_key(token)
                current.set_val(token)
                # print("\tCurrent node (after val):", current)
                current.insert_right(BinaryTree.BinaryTree.Node())
                current = current.right
                # print("\tAdded a right child. Current node is now right child:", current)
            elif token == ')':
                # print("\tCurrent node before updating:", current)
                current = current.parent
                # print("\tCurrent node updated to parent:", current)
            elif token in variables:
                # print("\tCurrent node (before val):", current)
                current.set_key(token)
                current.set_val(self.dict.find(token))
                # print("\tCurrent node (after val):", current)
                current = current.parent
                # print("\tCurrent updated to parent:", current)
            else:
                raise ValueError(f"{token} is an invalid token in the expression")
        return t