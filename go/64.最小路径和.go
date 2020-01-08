/*
 * @lc app=leetcode.cn id=64 lang=golang
 *
 * [64] 最小路径和
 */

// @lc code=start
func minPathSum(grid [][]int) int {
	
	m := len(grid)
	n := len(grid[0])
	// 按行，行边缘由上一步往下走
	for i := 1; i < m; i++ {
		grid[i][0] += grid[i-1][0]
	}
	// 按列，列边缘由上一步往右走
	for i:= 1; i < n; i++ {
		grid[0][i] += grid[0][i-1] 
	} 
	
	for i := 1; i < m ; i ++ {
		for j := 1; j < n; j++ {
			grid[i][j] += min(grid[i-1][j], grid[i][j-1])
		}
	}

	return grid[m-1][n-1]

}

func min(m, n int) int {
	if m > n {
		return n
	}else {
		return m
	}
}
// @lc code=end

