/*
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

左移就是把二进制中从右边替换零0
右移就是从左边替换零：如果是正数，替换即可
如果是负数，替换为1

把一个整数减去1之后再和原来的整数做位与运算，得到的结果相当于把该整数的
二进制表示中最右边的1变成0。
*/
package offer

import "testing"

func solution15(n int) int {
	count := 0
	for n != 0 {
		count++
		n = (n - 1) & n
	}
	return count
}

func TestSolution15(t *testing.T) {
	tes := []struct {
		in     int
		expect int
	}{
		{10, 2},
		{2, 1},

	}

	for _, v := range tes {
		actual := solution15(v.in)
		if v.expect != actual {
			t.Error("Expect: ", v.expect, "but: ", actual)
		}

	}
}
