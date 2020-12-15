/*
 * @lc app=leetcode.cn id=287 lang=golang
 *
 * [287] 寻找重复数
 给定一个包含 n + 1 个整数的数组 nums，
 其数字都在 1 到 n 之间（包括 1 和 n），
 可知至少存在一个重复的整数。假设只有一个重复的整数，
 找出这个重复的数。
1. 不能更改原数组（假设数组是只读的）。
2. 只能使用额外的 O(1) 的空间。
3. 时间复杂度小于 O(n2) 。
4. 数组中只有一个重复的数字，但它可能不止重复出现一次。
 */

 import "sort"

// @lc code=start
func findDuplicate(nums []int) int {
	/* 先排序，然后碰到第一个前后一样的就返回 */
	sort.Ints(nums)

	for i:=1;i<len(nums);i++ {
		if nums[i] == nums[i-1] {
			return nums[i]
		}
	}
	return -1

}
// @lc code=end

