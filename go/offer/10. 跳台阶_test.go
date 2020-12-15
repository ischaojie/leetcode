/*
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
*/
package offer

import "testing"

import "fmt"

func solution10(n int) int {
	if n == 1 {
		return n
	}
	dp := make([]int, n-1)
	dp = append(dp, 1)
	dp = append(dp, 2)
	for i := 3; i <= n; i++ {
		temp := dp[i-1] + dp[i-2]
		dp = append(dp, temp)
	}
	return dp[n]
}

func TestSolution10(t *testing.T) {
	fmt.Println(solution10(10))
	tes := []struct {
		in     int
		expect int
	}{
		{11, 5},
		{1, 1},
		{10, 10},
	}

	for _, v := range tes {
		actual := solution10(v.in)
		if actual != v.expect {
			t.Error("Expect:", v.expect, " but:", actual)
		}
	}
}
