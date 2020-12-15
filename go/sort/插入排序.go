package main

import "fmt"

func InsertSort(data []int) []int {

	for i := 1; i < len(data); i++ {
		pivot := data[i]
		for j := i - 1; j >= 0; j-- {
			if data[j] > pivot {
				data[j], data[j+1] = data[j+1], data[j]
			}else{
				data[j+1] = pivot
				break
			}
		}
	}

	return data
}

func main() {
	data := []int{12, 22, 3, 54, 32, 11, 34}
	fmt.Println(InsertSort(data))
}
