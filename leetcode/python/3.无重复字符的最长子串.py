#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        queue = []
        curr_len = 0
        max_len = 0

        for n in range(len(s)):
            if s[n] in queue:
                index = queue.index(s[n])
                # 移除重复位之前的
                queue = queue[index+1:]
                queue.append(s[n])
                curr_len = len(queue)
            else:
                queue.append(s[n])
                curr_len += 1
            # 更新最大长度
            if curr_len  > max_len:
                max_len = curr_len

        return max_len



# @lc code=end

