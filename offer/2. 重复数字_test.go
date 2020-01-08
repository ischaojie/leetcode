/*
1. 给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
*/

package offer

import (
	"testing"
)

// 1. 利用hash表判断 time: Q(n) space: Q(n)
func Solution(nums []int) bool {
	var hash = make(map[int]int)

	for _, v := range nums {
		//
		if _, ok := hash[v]; ok {
			return true
		}
		hash[v] = 1

	}

	return false

}

// 2. 先排序，然后判断前后两个是否一样

func TestSolution(t *testing.T) {
	nums := []struct {
		in     []int
		expect bool
	}{
		{[]int{2, 3, 1, 0, 2, 5, 3}, true},
		{[]int{3, 4, 2, 5}, false},
		{[]int{}, false},
	}

	for _, num := range nums {
		actual := Solution(num.in)
		if actual != num.expect {
			t.Error(actual, " but-> ", num.expect)
		}
	}

}
