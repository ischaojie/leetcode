#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        level = [root]
        res = []
        while level:
            tmp = []
            # 下一层
            next_level = []
            
            for node in level:
                tmp.append(node.val)
                # 将左右节点加入
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            level = next_level
        return res
# @lc code=end

