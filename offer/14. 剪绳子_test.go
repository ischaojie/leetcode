/*
剪绳子：求绳子任意剪m段之后的乘积最大
动态规划问题：
一刀将绳子剪成两段，那么此时的成绩最大等于左边的最大或者右边的最大中的一个
转移方程：
	长度为n的绳子剪断的最大乘积是
	dp[n] = max(dp[i]*dp[n-i]) | 0<i<n
*/
package offer

import (
	"testing"
)

func solution14(n int) int {
	if n == 2 {
		return 1
	}
	if n == 3 {
		return 2
	}

	dp := make([]int, n+1)
	dp[0] = 0
	dp[1] = 1
	dp[2] = 2
	dp[3] = 3
	max := 0
	for i := 4; i <= n; i++ {
		for j := 1; j <= i/2; j++ {
			// 从最小的问题开始，每次取乘积最大的
			temp := dp[j] * dp[i-j]
			if max < temp {
				max = temp
			}

		}
		dp[i] = max
	}
	return dp[n]
}

func TestSolution14(t *testing.T) {
	tes := []struct {
		in     int
		expect int
	}{
		{2, 1},
		{3, 2},
		{4, 4},
		{8, 18},
	}

	for _, v := range tes {
		actual := solution14(v.in)
		if actual != v.expect {
			t.Error(v.expect, " : ", actual)
		}
	}
}
