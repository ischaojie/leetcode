package offer

import (
	"fmt"
	"testing"
)

type ListNode struct {
	value int
	next  *ListNode
}

// 利用栈结构实现：先进后出
// 其实就是将链表转化为数组，然后从后向前输出
func solution5(header *ListNode) []int {
	var res []int

	for header != nil {
		res = append(res, header.value)
		header = header.next
	}

	// reverse
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}

// 利用递归实现
func solution5_2(header *ListNode) {

	if header != nil {
		if header.next != nil {
			solution5_2(header.next)
		}
		fmt.Println(header.value)
	}
}

func TestSolution5(t *testing.T) {

	nodes := []struct {
		in     *ListNode
		expect []int
	}{
		{&ListNode{3, &ListNode{4, &ListNode{2, &ListNode{5, nil}}}}, []int{5, 2, 4, 3}},
		{&ListNode{9, nil}, []int{9}},
		{nil, []int{}},
	}

	for _, n := range nodes {
		actual := solution5(n.in)
		for i, v := range actual {
			if v != n.expect[i] {
				t.Error("expect: ", n.expect, " acutal: ", actual)
			}
		}

	}

}
