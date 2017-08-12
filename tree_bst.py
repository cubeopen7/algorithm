# -*- coding: utf-8 -*-

from collections import Iterable
from tree_base import Node, Tree


class BinarySearchTree(Tree):
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            if isinstance(values, Iterable):
                for v in values:
                    self.insert(v)
            else:
                self.root = Node(values)

    def _insert(self, value, root):
        if root is None:
            root = Node(value)
            return root
        if value < root.value:
            root.left = self._insert(value, root.left)
        else:
            root.right = self._insert(value, root.right)
        return root

    # 插入元素
    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _find(self, value, root):
        if root is None:
            return False
        if value < root.value:
            return self._find(value, root.left)
        elif value > root.value:
            return self._find(value, root.right)
        else:
            return True

    # 查找元素
    def find(self, value):
        return self._find(value, self.root)

    def _find_min(self, root):
        if root is None:
            return
        if root.left is not None:
            root = self._find_min(root.left)
        return root

    def _delete(self, value, root):
        if root is None:
            return
        if value < root.value and root.left:
            root.left = self._delete(value, root.left)
        elif value > root.value and root.right:
            root.right = self._delete(value, root.right)
        else:
            if root.right is None:
                if root.left is None:
                    root = None
                else:
                    root.value = root.left.value
                    root.left = None
            else:
                parnet, child = None, root.right
                while True:
                    if child.left:
                        parnet = child
                        child = child.left
                    else:
                        if parnet is None:
                            root.value = child.value
                            root.right = child.right
                        else:
                            parnet.left = child.right
                            root.value = child.value
                        break
        return root

    # 删除元素
    def delete(self, value):
        self.root = self._delete(value, self.root)



if __name__ == "__main__":
    bst = BinarySearchTree("DBACEGF")
    print(bst.pre_order())
    print(bst.mid_order())
    print(bst.after_order())
    print(bst.find("F"))
    print(bst.find("H"))
    bst.delete("E")
    print(bst.pre_order())