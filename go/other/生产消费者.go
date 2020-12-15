package main

import "fmt"

func producer(c chan int) {
	for i :=0; i < 10; i++ {
		fmt.Printf("producer: %d\n", i)
		c <- i
	}
	// 等待生产完成关闭
	defer close(c)

}


func consumer(c chan int) {
	ok := true
	var p int
	for ok{
		// 还有生产的值，消费
		if p, ok = <- c; ok {
			fmt.Printf("get: %d\n", p)
		}
	}
}

func main() {
	c := make(chan int)

	go producer(c)
	consumer(c)
	/*
	producer: 0
	producer: 1
	get: 0
	get: 1
	......
	*/
}