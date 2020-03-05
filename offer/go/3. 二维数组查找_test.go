package offer

import "testing"

func TestSolution3(t *testing.T) {
	type Array struct {
		arr [][]int
		n   int
	}

	nums := []struct {
		in     Array
		expect bool
	}{
		{Array{arr: [][]int{}, n: 5}, false},
		{Array{arr: [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, n: 5}, true},
		{Array{arr: [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, n: 9}, true},
		{Array{arr: [][]int{{1, 2, 3}, {4, 5, 6}}, n: 7}, false},
	}

	for _, n := range nums {
		actual := solution(n.in.arr, n.in.n)
		if actual != n.expect {
			t.Error(n.expect, " but get-> ", actual)
		}
	}
}

// 从左下角开始找
func solution(array [][]int, n int) bool {
	if len(array) == 0 {
		return false
	}

	left, right, up, down := 0, len(array[0]), len(array)-1, len(array)

	for left < right && up < down {
		// 如果该行大于的话，减一行
		if array[up][left] > n {
			up--
			// 如果列小于的话，加一列
		} else if array[up][left] < n {
			left++
		} else {
			return true
		}
	}

	return false
}
