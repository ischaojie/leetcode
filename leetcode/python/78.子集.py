#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

"""
回溯法
"""

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], 0, nums)
        return self.res


    def backtrack(self, sol, first, nums):
        # 如果索引到末尾，加入返回
        if first == len(nums):
            self.res.append(sol)
            return
        # 索引向前，元素选择加入或者不加入
        self.backtrack(sol+[nums[first]], first+1, nums)
        self.backtrack(sol, first+1, nums)
# @lc code=end

