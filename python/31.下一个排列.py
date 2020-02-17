#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        i = n - 1
        # 如果前一个大于后一个，前进
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0 and nums[i] == max(nums):
            return nums.reverse()
        else:
            j = n - 1
            while j > i-1 and nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            re = nums[i:]
            for h in range(len(re)):
                nums[n-1-h] = re[h]
            return nums

# @lc code=end
