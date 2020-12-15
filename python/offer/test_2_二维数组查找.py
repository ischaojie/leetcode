""" [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
] """


def solution(arrs, num: int) -> bool:

    if len(arrs) == 0:
        return False
    # * 定位四个点
    left, right, up, down = 0, len(arrs[0]), len(arrs)-1, len(arrs)
    
    while left < right and up < down:
        # up--，从下往上
        if arrs[up][left] > num:
            up -= 1
        # left++，从左往右
        elif arrs[up][left] < num:
            left += 1
        else:
            return True
    return False

def test_solution():
    arrs = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    assert solution(arrs, 5) == True
    assert solution(arrs, 20) == False

