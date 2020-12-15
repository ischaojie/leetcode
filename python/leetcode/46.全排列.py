#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, first):
        # first代表每一层的计算
        # 当first到达终点，加入res
        if first == len(nums):
            self.res.append(nums[:])
        # 循环交换，将first分别置为其他元素
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(nums, first+1)
            nums[first], nums[i] = nums[i], nums[first]

        # 或者利用库函数 list(itertools.permutations(nums))
# @lc code=end
