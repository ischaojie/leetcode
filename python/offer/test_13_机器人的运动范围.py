class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # * 标记是否访问过
        visited = [[False for _ in range(n)] for _ in range(m)]

        # * 深度优先遍历
        def dfs(i, j, m, n, k, visited):
            # * 退出条件
            if i == m or j == n or sumK(i, j) > k or visited[i][j]:
                return 0

            # * 标记当前访问过
            visited[i][j] = True
            # * 向右和向下搜素
            return 1 + dfs(i+1, j, m, n, k, visited) + dfs(i, j+1, m, n, k, visited)

        def sumK(i, j):
            return i % 10 + i/10 + j % 10 + j / 10

        return dfs(0, 0, m, n, k, visited)
