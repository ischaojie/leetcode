/*
 * @lc app=leetcode.cn id=62 lang=golang
 *
 * [62] 不同路径
 */

// @lc code=start
func uniquePaths(m int, n int) int {
	/* 
	动态规划方程：
	dp[i][j] = dp[i-1][j] + dp[i][j-1] 
	*/
	dp := make([][]int, m)
	
	for i:=0;i<m;i++ {
		dp[i] = make([]int, n)
		for j:=0;j<n;j++{
			if i==0 || j == 0 {
				dp[i][j] = 1
			}else{
				dp[i][j] = dp[i][j-1] + dp[i-1][j]
			}
		}
	}
	return dp[m-1][n-1]
}
// @lc code=end

