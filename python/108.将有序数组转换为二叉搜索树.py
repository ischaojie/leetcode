#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 利用递归实现
        if nums is None:
            return None
        start = 0
        end = len(nums) - 1
        mid = (end-start) >> 1
        if end < start:
            return None
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[start:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:end+1])
        return root
# @lc code=end

