#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        # 快指针用来遍历，如果数字不是0，将当前数组赋值给慢指针，慢指针向前走一步
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # 走完了将后面的补零
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        
# @lc code=end

