
def solution(n):
    """
    传统解法
    """
    if n <= 1:
        return n
    return solution(n-1) + solution(n-2)


def solution2(n):
    """
    使用动态规划（递增法）
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def solution3(n):
    """
    使用生成器
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a


for i in solution3(10):
    print(i, end=' ')


def test_solution():
    assert solution(8) == 21
