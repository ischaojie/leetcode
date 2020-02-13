#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(sr, sub):
            if not sr:
                res.append(sub)

            for i in range(len(sr)):
                # 如果是回文
                if sr[:i+1] == sr[i::-1]:
                    # 回溯
                    backtrack(sr[i+1:], sub+[sr[:i+1]])

        backtrack(s, [])
        return res
# @lc code=end
