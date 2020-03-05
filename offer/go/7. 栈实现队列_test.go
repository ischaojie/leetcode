package offer

import (
	"fmt"
	"sync"
	"testing"
)

type Stack struct {
	lock sync.Mutex
	s    []int
	len  int
}

func NewStack() *Stack {
	return &Stack{sync.Mutex{}, []int{}, 0}
}

func (s *Stack) Push(v int) {
	s.lock.Lock()
	defer s.lock.Unlock()

	s.s = append(s.s, v)
	s.len++
}

func (s *Stack) Pop() int {
	s.lock.Lock()
	defer s.lock.Unlock()

	if s.len == 0 {
		return -1
	}

	res := s.s[s.len-1]
	s.s = s.s[:s.len-1]
	s.len--
	return res
}

type Queue struct {
	instack  *Stack
	outstack *Stack
}

func NewQueue() *Queue {
	return &Queue{
		instack:  &Stack{},
		outstack: &Stack{},
	}
}

func (q *Queue) Push(node int) {
	q.instack.Push(node)
}

func (q *Queue) Pop() int {
	for q.instack.len > 0 {
		q.outstack.Push(q.instack.Pop())
	}

	return q.outstack.Pop()
}

func TestQueue(t *testing.T) {

	tes := []int{1, 2, 3, 4}
	queue := NewQueue()
	for _, v := range tes {
		queue.Push(v)
	}
	for queue.Pop() != -1 {

	}
	fmt.Println(queue.Pop())

}

func TestSack(t *testing.T) {

	tes := []int{1, 2, 3, 4}
	stack := NewStack()
	for _, v := range tes {
		stack.Push(v)
	}
	i := 1
	for stack.len > 0 {
		p := stack.Pop()
		if tes[len(tes)-i] != p {
			t.Error(tes[len(tes)-i], "but-> ", p)
		}
		i++
	}
}
