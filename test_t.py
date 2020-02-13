
# 子集


def solution(nums):
    res = []
    backtrack(0, [], nums)
    return res

    def backtrack(first, sol, nums):
        if first == len(nums):
            res.append(sol)

        backtrack(first+1, sol+[nums[first]], nums)
        backtrack(first+1, sol, nums)

# 最多出现一次
# [1, 2, 2, 1, 3]


def solution2(nums):
    res = {}
    for n in nums:
        if res.get(n):
            res[n] = 0
        else:
            res[n] = 1
    for k, v in res.items():
        if v == 1:
            return k



# 矩阵置零
def solution3(nums):

    m = len(nums)
    n = len(nums[0])

    rows, cols = set(), set()

    for i in range(m):
        for j in range(n):
            if nums[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                nums[i][j] = 0


# 链表k次反转
def solution4(node, k):
    pre = *Node

    cur = node
    i = 0
    while i < k:
        temp = cur.next

        cur.next = pre

        pre = cur

        cur = temp
        i += 1
    return pre