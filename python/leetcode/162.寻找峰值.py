#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums) -> int:

        left, right = 0, len(nums)-1

        if len(nums) <= 1:
            return 0

        while left < right:
            if nums[left] > nums[left+1]:
                return left
            left += 1
        if left == right:
            return left

def test_so():
    nums = [1, 2, 3, 1, 2, 3]
    print(Solution().findPeakElement(nums))

if __name__ == "__main__":
    test_so()
        
# @lc code=end

