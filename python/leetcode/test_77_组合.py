# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

class Solution:
    """
    套用回溯法框架（排列和子集问题）
    """
    def combine(self, n: int, k: int):
        self.result = []
        self.backtrack(1, [], n, k)
        return self.result

    def backtrack(self, start, track, n, k):
        """
        start 代表开始位置
        track 代表路径
        """

        # *如果路径中元素到达 k 个，加入结果集
        if k == len(track):
            self.result.append(track[:])
            return
        # 从 1 到 n
        for i in range(start, n+1):
            track.append(i)
            # 注意这里是 i+1，与子集问题相同
            # 保证 start 从后面开始，避免重复
            self.backtrack(i+1, track, n, k)
            track.pop()

def test_solution():
    result = Solution().combine(3, 2)
    expected = [[1,2],[1,3],[2,3]]
    assert result == expected
