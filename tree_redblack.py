# -*- coding: utf-8 -*-

RED = 1
BLACK = 0

class RedBlackNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.num = 1
        self.color = RED


class RedBlackTree(object):
    def __init__(self, value=None):
        self.root = None

    def number(self, node):
        if node is None:
            return 0
        return node.num

    def is_red(self, node):
        if node is None:
            return False
        return node.color == RED

    def left_rotate(self, node):
        b = node.right
        node.right = b.left
        b.left = node
        b.color = node.color
        node.color = RED
        b.num = node.num
        node.num = self.number(node.left) + self.number(node.right) + 1
        return b

    def right_rotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        x.num = node.num
        node.num = self.number(node.left) + self.number(node.right) + 1
        return x

    def flip_colors(self, node):
        node.left.color = BLACK
        node.right.color = BLACK
        node.color = RED

    def _insert(self, node, value):
        if node is None:
            return RedBlackNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        if self.is_red(node.right) and ~self.is_red(node.left):
            node = self.left_rotate(node)
        elif self.is_red(node.left) and self.is_red(node.left.left):
            node = self.right_rotate(node)
        elif self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        node.num = self.number(node.left) + self.number(node.right) + 1
        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = BLACK


if __name__ == "__main__":
    num_list = [5,3,8,2,1,9,7,6,4]
    tree = RedBlackTree()
    for i in num_list:
        tree.insert(i)
    a = 1