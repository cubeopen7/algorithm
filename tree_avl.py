# -*- coding: utf-8 -*-

from collections import Iterable
from tree_base import Tree, AVLNode


class AVLTree(Tree):
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            if isinstance(values, Iterable):
                for v in values:
                    self.insert(v)
            else:
                self.root = AVLNode(values)

    def _height(self, node):
        if node is not None:
            return node.height
        else:
            return -1

    def left_rotate(self, node):
        b = node.right
        node.right = b.left
        b.left = node
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        b.height = max(self._height(b.left), self._height(b.right)) + 1
        return b

    def right_rotate(self, node):
        b = node.left
        node.left = b.right
        b.right = node
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        b.height = max(self._height(b.left), self._height(b.right)) + 1
        return b

    def left_right_rotate(self, node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_left_rotate(self, node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def _find(self, value, root):
        if root is None:
            return None
        if value < root.value:
            return self._find(value, root.left)
        elif value > root.value:
            return self._find(value, root.right)
        else:
            return root

    def _find_min(self, node):
        if node.left is not None:
            return self._find_min(node.left)
        else:
            return node

    def find(self, value):
        node = self._find(value, self.root)
        if node is None:
            return False
        return True

    def _insert(self, value, node):
        if node is None:
            node = AVLNode(value)
            return node
        if value < node.value:
            node.left = self._insert(value, node.left)
            if self._height(node.left) - self._height(node.right) == 2:
                if value < node.left.value:
                    node = self.right_rotate(node)
                else:
                    node = self.left_right_rotate(node)
        else:
            node.right = self._insert(value, node.right)
            if self._height(node.left) - self._height(node.right) == -2:
                if value >= node.right.value:
                    node = self.left_rotate(node)
                else:
                    node = self.right_left_rotate(node)
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return node

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _delete(self, value, node):
        if node is None:
            return
        if value < node.value:
            node.left = self._delete(value, node.left)
            if (self._height(node.right) - self._height(node.left)) == 2:
                if self._height(node.right.left) > self._height(node.right.right):
                    node = self.right_left_rotate(node)
                else:
                    node = self.left_rotate(node)
            node.height = max(self._height(node.left), self._height(node.right)) + 1
        elif value > node.value:
            node.right = self._delete(value, node.right)
            if (self._height(node.left) - self._height(node.right)) == 2:
                if self._height(node.left.left) > self._height(node.left.right):
                    node = self.right_rotate(node)
                else:
                    node = self.left_right_rotate(node)
            node.height = max(self._height(node.left), self._height(node.right)) + 1
        else:
            if node.right and node.left:
                sub_min_node = self._find_min(node.right)
                node.value = sub_min_node.value
                node.right = self._delete(node.value, node.right)
                node.height = max(self._height(node.left), self._height(node.right)) + 1
                if (self._height(node.left) - self._height(node.right)) == 2:
                    if self._height(node.left.left) > self._height(node.left.right):
                        node = self.right_rotate(node)
                    else:
                        node = self.left_right_rotate(node)
                    node.height = max(self._height(node.left), self._height(node.right)) + 1
            elif node.right:
                node = node.right
            else:
                node = node.left
        return node

    def delete(self, value):
        self.root = self._delete(value, self.root)


if __name__ == "__main__":
    avl = AVLTree("DBACEGF")
    print(avl.pre_order())
    print(avl.mid_order())
    print(avl.after_order())
    print(avl.find("F"))
    print(avl.find("H"))
    avl.delete("E")
    print(avl.pre_order())