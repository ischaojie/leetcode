/*
 * @lc app=leetcode.cn id=300 lang=golang
 *
 * [300] 最长上升子序列
 */

// @lc code=start
func lengthOfLIS(nums []int) int {
	/* 状态转移方程
	dp[i]代表前i个数字的最长序列长度
	dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
	*/
	if len(nums) == 0 {
		return 0
	}
	dp := make([]int, len(nums))
	for v, _ := range nums {
		dp[v] = 1
	}	
	res := 0
	for i, _ := range nums {
		for j:= 0; j < i; j++ {
			// 如果当前还是递增的
			if nums[i] > nums[j] {
				if dp[i] < dp[j] + 1 {
					dp[i] = dp[j] + 1
				}
			}
		}
		if res < dp[i] {
			res = dp[i]
		}
	}
	return res

	
}
// @lc code=end

