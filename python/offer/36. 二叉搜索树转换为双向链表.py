

class Solution:

    def __init__(self):
        self.head = None
        self.pre = None
        self.tail = None

    def treeToDoublyList(self, root):
        if not root:
            return None
        self.treeList(root)

        # 头尾相连
        self.head.left = self.tail
        self.tail.right = self.head

        return self.head

    def treeList(self, node):

        if not node:
            return None

        self.treeList(left)

        if self.pre is None:
            self.head = node
        else:
            # 指向后
            self.pre.right = node
        # 指向前
        node.left = self.pre

        self.pre = node
        self.tail = node

        self.treeList(right)
