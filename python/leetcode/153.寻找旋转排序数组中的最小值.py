#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        mid = 0

        # 找到中间的数
        while left < right:
            if nums[left] > nums[left+1]:
                mid = left
            left += 1
        
        if mid == len(nums)-1:
            return nums[0]
        
        if nums[0] < nums[mid+1]:
            return nums[0]
        else:
            return nums[mid+1]
        
# @lc code=end

