"""
多抓鱼2020笔试题
"""

"""
1. 将列表切分成 n 等份
"""

def _chunk(arr: list, n: int):

    for i in range(0, len(arr), n):
        yield arr[i: i+n]


def chunk(arr: list, n: int):
    return list(_chunk(arr, n))


"""
2. BPG 树
"""


"""
3. 验证栈序列
leetcode 946
"""