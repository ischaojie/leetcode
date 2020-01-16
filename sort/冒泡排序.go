package main

import (
	"fmt"
)

func BubbleSort(data []int) []int{
	for i := 0; i <= len(data); i++ {
		for j := i + 1; j < len(data); j++ {
			if data[j] < data[i] {
				data[i], data[j] = data[j], data[i]
			}
		}
	}
	return data
}

func main() {
	data := []int{1, 2, 22, 11, 32, 3, 5, 14}
	fmt.Printf("sorted: %d\n", BubbleSort(data))
}
