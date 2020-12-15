

def solution(arr: list[int]) -> bool:
    """
    docstring
    """
    hashs = {}

    for a in arr:
        if hashs.get(a):
            return True
        hashs[a] = 1
    return False


def test_solution():
    assert solution([1, 2, 2, 3]) == True
    assert solution([2,3,1,6,4]) == False
