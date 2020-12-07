def solution(n):
    """
    与斐波那契数列相同
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a