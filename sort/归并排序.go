/*
归并排序：
稳定（最坏最好平均情况下时间复杂度一样）
时间复杂度O(nlogn)
*/

package main

import "fmt"

func main() {
	data := []int{1, 22, 2, 65, 23, 3, 67, 122, 6, 9, 11}
	fmt.Println(MergeSort(data))

}

func MergeSort(data []int) []int {
	/*
	利用递归，先对半分解，然后依次合并
	*/
	if len(data) < 2 {
		return data
	}
	// 分解
	middle := len(data) / 2
	left := MergeSort(data[:middle])
	right := MergeSort(data[middle:])

	// 合并
	return Sort(left, right)
}

func Sort(start, end []int) []int {
	/*
		合并排好序的左右半边：
		依次在左右半边放个哨兵，比较大小，小的加入结果，然后后移
	*/
	i, j := 0, 0
	var result []int
	for i < len(start) && j < len(end) {
		if start[i] > end[j] {
			result = append(result, end[j])
			j++

		} else {
			result = append(result, start[i])
			i++
		}
	}
	result = append(result, start[i:]...)
	result = append(result, end[j:]...)
	return result
}
