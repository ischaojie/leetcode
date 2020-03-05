package offer

import "testing"

// 递归会导致很多重复计算
func solution9(n int) int {

	if n <= 0 {
		return 0
	}

	if n == 1 {
		return 1
	}
	return solution9(n-1) + solution9(n-2)

}

// 自上而下
func solution9_2(n int) int {
	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	one, two := 1, 0
	res := 0
	for i := 2; i <= n; i++ {
		res = one + two

		two = one
		one = res
	}
	return res
}

func TestSolution9(t *testing.T) {
	res := []struct {
		in     int
		expect int
	}{
		{1, 1},
		{0, 0},
		{10, 55},
	}

	for _, v := range res {
		actual := solution9(v.in)
		if actual != v.expect {
			t.Errorf("Expect %d, but: %d", v.expect, actual)
		}
	}
}
