class Solution:
    def exchange(self, nums: list[int]) -> list[int]:
        # i、j分别从左右两边
        i, j = 0, len(nums)-1
        # x&1 就相当于 x%2
        while i < j:
            # 左边找偶数
            while i < j and nums[i] & 1 == 1:
                i += 1
            # 右边找奇数
            while i < j and nums[j] & 1 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums