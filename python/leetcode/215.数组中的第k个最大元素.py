#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
# 快排算法实现
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return
        pivot = nums[0]
        less_part = [i for i in nums[1:] if i <= pivot]
        more_part = [i for i in nums[1:] if i > pivot]

        if len(more_part) == k-1:
            return pivot
        elif len(more_part) > k-1:
            return self.findKthLargest(more_part, k)
        else:
            return self.findKthLargest(less_part, k-len(more_part)-1)
        
# @lc code=end

