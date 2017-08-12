# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class AVLNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class Tree(object):
    def insert(self, value):
        pass

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def pre_order(self):
        if self.root is None:
            return []
        result_list = []
        node_stack = [self.root]
        while node_stack:
            node = node_stack.pop()  # 压出最后一个元素
            result_list.append(node.value)
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
        return result_list

    def mid_order(self):
        if self.root is None:
            return []
        result_list = []
        node_stack = []
        node = self.root
        while node_stack or node:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            result_list.append(node.value)
            node = node.right
        return result_list

    def after_order(self):
        if self.root is None:
            return []
        result_list = []
        node_stack = []
        node = self.root
        node_mark = None
        while node_stack or node:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            if not node.right or node.right is node_mark:
                result_list.append(node.value)
                node_mark = node
                node = None
            else:
                node_stack.append(node)
                node = node.right
        return result_list