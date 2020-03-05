package main

import "fmt"

func main() {

	a := []int{1,2,3,4,5,6}
	s := a[2:4]

	s[0] = 100

	fmt.Println(s)
	fmt.Println(a)


}