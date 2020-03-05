package offer

import (
	"fmt"
	"sync"
)

type singleton struct {
	name string
}

var (
	instance *singleton
	once     sync.Once
)

func Instance() *singleton {
	once.Do(func() {
		instance = &singleton{}
		instance.name = "first singleton"
	})

	return instance

}

func main() {
	ins := Instance()
	fmt.Println(ins.name)

	ins2 := Instance()
	fmt.Println(ins2.name)
}
