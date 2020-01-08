#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    # 递归版本
    def isMatch(self, s: str, p: str) -> bool:
        # 1. 当p为空时候，判断s是否为空，若是，匹配成功，不是，匹配失败
        if not p:
            return not s
        # 2. 判断第一位是否匹配：如果s和p的第一位相同或者p的第一位为.的时候
        if s and (p[0] == '.' or s[0] == p[0]):
            return self.isMatch(s[1:], p[1:])
        
        # 3. 如果p中有*，第二位为*，两种情况：
        if len(p) > 1 and p[1] == '*':
            # 3.1 首位匹配
            if s and (p[0] == '.' or s[0] == p[0]):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            # 3.2 其他的
            return self.isMatch(s, p[2:])
        return False
# @lc code=end

