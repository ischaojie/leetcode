#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start


class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        if m == 0:
            return False
        # mark用来标记是否被访问过
        mark = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 找到了
                if board[i][j] == word[0]:
                    # 标记已经访问
                    mark[i][j] = 1

                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        mark[i][j] = 0

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        # 上下左右搜索
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            # 找到该节点
            if cur_i >= 0 and cur_j >= 0 and cur_i < len(board) and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:

                # 如果已经被标记过，继续
                if mark[cur_i][cur_j] == 1:
                    continue

                # 标记为访问
                mark[cur_i][cur_j] = 1

                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    mark[cur_i][cur_j] = 0
        return False

# @lc code=end
