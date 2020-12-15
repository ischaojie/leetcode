#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(k) = max(f(k – 2) + Ak, f(k – 1))
        cur, pre = 0, 0
        for n in nums:
            cur, pre = max(pre+n, cur), cur
        return cur
        
# @lc code=end

