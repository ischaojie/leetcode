#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:

        INT_MAX = 2**31-1
        INT_MIN = -2**31
        str = str.lstrip()  # 清除空格
        import re
        num_re = re.compile(r'^[\+\-]?\d+')  # 正则匹配
        num = num_re.findall(str)
        num = int(*num) # 解包
        return max(min(num, INT_MAX), INT_MIN)
        
# @lc code=end

