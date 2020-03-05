package offer

import (
	"fmt"
	"testing"
)

type TreeNode struct {
	value int
	left  *TreeNode
	right *TreeNode
}

func TestSolution6(t *testing.T) {
	type Tree struct {
		pre []int
		in  []int
	}
	trees := []struct {
		in     Tree
		expect *TreeNode
	}{
		// {Tree{[]int{}, []int{}}, nil},
		{
			Tree{[]int{1, 2, 4, 7, 3, 5, 6, 8}, []int{4, 7, 2, 1, 5, 3, 8, 6}},
			&TreeNode{1,
				&TreeNode{2, &TreeNode{4, nil, &TreeNode{7, nil, nil}}, nil},
				&TreeNode{3, &TreeNode{5, nil, nil}, &TreeNode{6, &TreeNode{8, nil, nil}, nil}}},
		},
	}

	for _, v := range trees {
		// actual := solution6(v.in.pre, v.in.in)
		// fmt.Println(actual)
		fmt.Println(v.expect)
	}
}

//
func solution6(pre, in []int) *TreeNode {
	tree := &TreeNode{pre[0], nil, nil}

	var mid int
	for i, v := range pre {
		if v == 0 {
			mid = i
		}
	}

	tree.left = solution6(pre[1:mid+1], in[:mid])
	tree.right = solution6(pre[mid+1:], in[mid+1:])
	return tree
}
