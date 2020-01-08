package main

import "testing"

import "fmt"

func TestInt(t *testing.T) {
	ints := make([]int, 5*[1])
	fmt.Println(ints)
}
