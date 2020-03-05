# 只出现一次的字符
class Solution:

    def __init__(self):
        self.words = []
    
    def solution(self):
        import collections
        hashs = collections.Counter(self.words)  # 统计字符次数
        for w in self.words:
            if hashs[w] == 1:
                return w
        return '#'
    
    def insert(self, char):
        self.words.append(char)
    


# 美团
# 最长回文子串

# 知乎
# 二维数组0行列置0
def solution(nums):
    m = len(nums)
    n = len(nums[0])
    rows, column = set(), set()

    for i in range(m):
        for j in range(n):
            if nums[i][j] == 0:
                rows.add(i)
                column.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in column:
                nums[i][j] = 0

    return nums

# 探探
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

# 知乎
# 链表k次反转
def solution4(root, k):
    # tail每次移动k个大小
    aha = ListNode(0)
    aha.next = root

    pre, tail = aha, aha

    while tail:
        i = 0
        while i < k:
            tail = tail.next
            i += 1
        
        root = pre.next
        while pre.next != tail:
            # cur断链
            cur = pre.next
            pre.next = cur.next

            # 插入到tail后面
            cur.next = tail.next
            tail.next = cur
        
        pre, tail = root, root
    
    return aha.next
    






    


# 买卖股票最佳时机
def solution5(prices):
    if len(prices) <= 1:
        return 0

    min = prices[0]
    max = 0
    for price in prices:
        # 当前最大和今天的减去之前最小的哪个大
        if max < price - min:
            max = price - min
        # 找最小
        if min > price:
            min = price
    return max
