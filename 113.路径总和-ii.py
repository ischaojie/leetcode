#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        # 利用队列
        queue = [([root.val], root)]
        res = []

        while queue:
            v, node = queue.pop(0)
            # 判读和是不是要找的
            if not node.left and not node.right and sum(v) == sum_:
                res.append(v)
            if node.left:
                queue.append((v+[node.left.val], node.left))
            if node.right:
                queue.append((v+[node.right.val], node.right))
        return res

        
# @lc code=end

