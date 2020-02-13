#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i 代表0
        # j 代表2
        i, j, k = 0, len(nums)-1, 0

        while k <= j:
            # 把0放在前面
            # 然后i往后走
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i+=1
                k+=1
            # 把2放在后面
            # 然后j往前走
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1
# @lc code=end
