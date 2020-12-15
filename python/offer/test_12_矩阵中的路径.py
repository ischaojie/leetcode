

def solution(board: list[list[str]], word: str):
    """
    利用DFS+剪枝
    """
    # * dfs
    def dfs(i, j, k):
        # * 如果当前元素无法匹配，找下一个
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        board[i][j] = ''
        # * 搜索四个方向
        res = dfs(i-1, j, k+1) or dfs(i+1, j, k +
                                      1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
        board[i][j] = word[k]

        return res

    # * 循环
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
