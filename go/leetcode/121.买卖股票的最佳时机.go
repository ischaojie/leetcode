/*
 * @lc app=leetcode.cn id=121 lang=golang
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
func maxProfit(prices []int) int {
	/* 
	动态规划方程:
	前i天的最大收益 = max{ 前i-1天的最大收益，当天的价格-前i-1天的最低收益 }
	*/
    if len(prices) <= 1{
		return 0
	}
	min := prices[0]
	max := 0
	for i:=1; i < len(prices);i++ {
		// 当天最高利润=当前价格-之前的最小价格
		// 然后比较每天的最大利润
		if max < prices[i]-min {
			max = prices[i]-min
		}
		// 最今天之前的最小价格
		if min > prices[i] {
			min = prices[i]
		}
	}
	return max
}
// @lc code=end

