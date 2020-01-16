package main

import "fmt"

func SelectSort(data []int) []int {
	for i := 0; i < len(data); i++ {
		// 将最小值设为i
		min := i
		// 依次与后面的数比较，小的话设为min
		for j := i + 1; j < len(data); j++ {
			if data[j] < data[min] {
				min = j
			}
		}
		// 交换两个值，将min放在前面，接着进行下一轮
		data[min], data[i] = data[i], data[min]
	}
	return data
}

func main() {
	data := []int{1,22, 3, 54, 32, 11, 34}
	fmt.Println(SelectSort(data))
}
