#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root, root)
        
    def ismirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.ismirror(t1.left, t2.right) and self.ismirror(t1.right, t2.left)
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]

        while queue:
            node1 = queue.pop()
            node2 = queue.pop()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False

            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)


# @lc code=end

