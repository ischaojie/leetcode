def coinChange(coins: list[int], amount: int):

    # dp[n] 代表 凑出 n 所需的最少硬币数
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 初始化为正无穷
        res = float("INF")
        for coin in coins:
            # 子问题
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            # 状态转移 function
            res = min(res, 1 + subproblem)
        return res if res != float("INF") else -1

    return dp(amount)

def test_coinChange():
    assert coinChange([1,2,5], 11) == 3
