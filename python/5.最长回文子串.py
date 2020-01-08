#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return ""
    #     res = ""
    #     n = len(s)
    #     dp = [[0] * n for _ in range(n)]

    #     max_len = float("-inf")
    #     for i in range(n):
    #         for j in range(i + 1):
               
    #             if s[i] == s[j] and (i-j<2 or dp[j+1][i-1]):
    #                 dp[j][i] = 1
    #             if dp[j][i] and max_len < i+1-j:
    #                 res = s[j:i+1]
    #                 max_len = i+1-j
    #     return res

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2: return s
        max_len = 1
        res = s[0]

        for i in range(size):
            odd, odd_len = self.center_spread(s, size, i, i)
            even, even_len = self.center_spread(s,size, i, i+1)
           # 比较奇数情况下和偶数情况下哪个大
            cur_max = odd if odd_len >= even_len else even
            if len(cur_max) > max_len:
                max_len = len(cur_max)
                res = cur_max
        return res
    
    # 中心扩散
    def center_spread(self, s, size, left, right):
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right], right-left-1
        
# @lc code=end

