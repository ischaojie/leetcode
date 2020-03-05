#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左右指针
        left = 0
        right = len(height) - 1
        # 最大面积
        max_area = 0
        while left < right:
            # b是间距
            b = right-left
            # 如果左边高度低
            # 左边指针右移
            if height[left] <= height[right]:
                h = height[left]
                left += 1
            # 如果右边高度低
            # 右边指针左移
            elif height[left] > height[right]:
                h = height[right]
                right -= 1
            # 赋值最大面积
            area = b * h
            if max_area < area:
                max_area = area
        return max_area

# @lc code=end
