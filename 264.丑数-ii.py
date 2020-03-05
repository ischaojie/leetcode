#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 三指针法
        # 看不懂看不懂
        dp = [0] * n
        dp[0] = 1
        l2 = l3 = l5 = 0
        for i in range(1, n):
            dp[i] = min(dp[l2]*2, dp[l3]*3, dp[l5]*5)
            if dp[l2]*2 <= dp[i]:
                l2 += 1
            if dp[l3]*3 <= dp[i]:
                l3 += 1
            if dp[l5]*5 <= dp[i]:
                l5 += 1
        return dp[-1]
    
    def nthUglyNumber2(self, n: int) -> int:
        # 最小堆实现
        import heapq
        heap = []
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            # 每次都 获得最小的
            res = heapq.heappop(heap)
            l2, l3, l5 = res*2, res*3, res*5
            for n in [l2, l3, l5]:
                heapq.heappush(n)
        return res
        
# @lc code=end

