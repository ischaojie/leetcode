/*
快速排序:
*/
package main

func main() {

}

func QuickSort() {

}

func partition(data []int) {

	p := data[0]
	i := 0
	for j := i + 1; j < len(data); j++ {
		if data[j] < p {
			i++
			// 交换两个值
			data[j], data[i] = data[i], data[j]
		}
	}



}
