# 基本框架

"""
def binary_search(nums: list[int], target: int):
    left, right = 0, ...

    while ...:
        # 为啥不写成(left+right)//2
        # 防止 左右相加太大了导致溢出
        mid = left + (right - left) // 2
        if nums[mid] == target:
            ...
        elif nums[mid] < target:
            left = ...
        elif nums[mid] > target:
            right = ...
    return ...
"""


def binary_search(nums: list[int], target: int) -> int:
    # right=len(nums)-1，说明
    # 搜索区间为两端都闭合
    left, right = 0, len(nums) - 1
    # 两端闭合，所有 left <= right
    # 如果一开一闭，就是 left < right
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 注意为 mid+1
            # 因为搜索区间闭合，所以 mid 已经搜索过
            # 从下一个开始
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 没有找到，返回-1
    return -1


def test_binary_search():
    assert binary_search([1, 2, 4, 3, 5], 2) == 1
    assert binary_search([1, 2, 4, 3, 5], 1) == 0


def left_bound(nums, target):
    # 现在是开闭区间
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        # 找到 target，不立即返回
        # 缩小搜索右界，不断向左收缩
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 返回左边界
    return left

def test_left_bound():
    assert left_bound([1,2,2,2,3], 2) == 1
    assert left_bound([1,1,1,2,3], 1) == 0
