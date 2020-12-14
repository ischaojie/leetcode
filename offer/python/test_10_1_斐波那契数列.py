def solution(n):
    """
    传统解法
    """
    if n <= 1:
        return n
    return solution(n - 1) + solution(n - 2)


def solution2(n: int) -> int:
    """
    使用备忘录
    """
    if n < 1:
        return 0

    # 备忘录
    mem = [0 for _ in range(n + 1)]

    def helper(mem, n):
        if n == 1 or n == 2:
            return 1
        # 如果存在的话直接取即可
        if mem[n]:
            return mem[n]
        # 递归
        mem[n] = helper(mem, n - 1) + helper(mem, n - 2)
        return mem[n]

    return helper(mem, n)


def solution3(n):
    """
    使用动态规划，db相当于一个备忘录
    """
    if n == 1 or n == 2:
        return 1
    # dp备忘录
    dp = [0 for _ in range(n + 1)]

    dp[1] = dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def solution4(n):
    """
    使用生成器
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def test_solution():
    assert solution2(8) == 21
    assert solution3(8) == 21
