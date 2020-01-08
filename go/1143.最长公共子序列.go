/*
 * @lc app=leetcode.cn id=1143 lang=golang
 *
 * [1143] 最长公共子序列
 */

// @lc code=start
func longestCommonSubsequence(text1 string, text2 string) int {
	m := len([]rune(text1))
	n := len([]rune(text2))
	dp := make([][]int, m)
	for i := 1; i <= m; i++ {
		dp[i] = make([]int, n)
		
		for j := 1; j <= n; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			}else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[m-1][n-1]
}

func max(m, n int) int {
	if m > n{
		return m
	}else {
		return n
	}
}
// @lc code=end

