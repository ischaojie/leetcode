class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        找到规律即可
        """
        # * 如果 n = 0的话，结果都为 1
        if n == 0:
            return 1
        # * 如果 n < 0，转为正数计算
        if n < 0:
            return self.myPow(1/x, -n)
        # * n > 0
        # 如果n是偶数，可以转成：
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        # 如果是奇数
        else:
            return self.myPow(x*x, n/2)*x
