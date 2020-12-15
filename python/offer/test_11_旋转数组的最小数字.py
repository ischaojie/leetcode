def solution(arr):
    """
    利用二分查找
    """
    left, right = 0, len(arr) - 1
    while left < right:
        # 找中间
        mid = (left+right)//2
        # 如果中间的大，说明中间左边都不是要找的
        # 从右边找
        if arr[mid] > arr[right]:
            left = mid+1
        elif arr[mid] == arr[right]:
            right -= 1
        # 从左边找
        else:
            right = mid
    return arr[left]


def test_solution():
    assert solution([3,4,5,1,2]) == 1
