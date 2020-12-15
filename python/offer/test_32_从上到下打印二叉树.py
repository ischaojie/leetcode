class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

"""
从上到下按层打印
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        level = [root]
        res = []
        while level:
            temp = [] # temp用来临时存放每一层的数据
            next_level = [] # 表示下一层节点
            for node in level:
                temp.append(node.val)
                # 将节点的左右子节点加入
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
    
            level = next_level
            res.append(temp)
        return res
