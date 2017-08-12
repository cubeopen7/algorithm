# -*- coding: utf-8 -*-


class Node23(object):
    def __init__(self, value, value2=None):
        self.value = value
        self.value2 = value2
        self.left = None
        self.middle = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None and self.middle is None

    def is_full(self):
        return self.value is not None and self.value2 is not None

    def has_value(self, value):
        if self.value == value or self.value2 == value:
            return True
        return False

    def get_branch(self, value):
        if value < self.value:
            return self.left
        elif self.value2 is None:
            return self.middle
        elif value < self.value2:
            return self.middle
        else:
            return self.right


class Tree23(object):
    def __init__(self, value=None):
        self.root = None

    def _find(self, value, node):
        if node is None:
            return
        if node.has_value(value):
            return node
        else:
            return self._find(value, node.get_branch(value))

    def find(self, value):
        return self._find(value, self.root)

    def _split_node(self, value, node, sub):
        new_node = Node23(None, None)
        if value < node.value:
            p_value = node.value
            node.value = value
            new_node.value = node.value2
            if sub is not None: # 上溢插入父结点的情况
                new_node.left = node.middle
                new_node.middle = node.right
                node.middle = sub
        elif value > node.value2:
            p_value = node.value2
            new_node.value = value
            if sub is not None:
                new_node.left = node.right
                new_node.middle = sub
        else:
            p_value = value
            new_node.value = node.value
            if sub is not None:
                new_node.left = sub
                new_node.middle = node.right
        node.value2 = None
        return p_value, new_node

    def _add_to_node(self, value, node, sub):
        if node.is_full():
            return self._split_node(value, node, None)
        else:
            if value < node.value:
                node.value2 = node.value
                node.value = value
                if sub is not None:
                    node.right = node.middle
                    node.middle = sub
            else:
                node.value2 = value
                if sub is not None:
                    node.right = sub
            return None, None

    def _insert(self, value, node):
        if node.has_value(value):
            return None, None
        elif node.is_leaf():
            return self._add_to_node(value, node, None)
        else:
            branch = node.get_branch(value)
            p_value, p_ref = self._insert(value, branch)
            if p_value is None:  # 没有上溢值
                return None, None
            else:
                return self._add_to_node(p_value, node, p_ref)

    def insert(self, value):
        if self.root is None:
            self.root = Node23(value)
            p_value, p_ref = self._insert(value, self.root)
            if p_value is not None:
                new_node = Node23(p_value, None)
                new_node.left = self.root
                new_node.middle = p_ref
                self.root = new_node