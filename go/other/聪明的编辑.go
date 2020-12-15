package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	for n > 0 {
		word := ""
		fmt.Scanf("%s", &word)
		
		res := []rune{}
		for i, w := range word {
			if len(res) < 2 {
				res = append(res, w)
				continue
			}

			if len(res) >= 2 {
				if w == res[i-1] && w == res[i-2] {
					continue
				}
			}
			if len(res) >= 3 {
				if w == res[i-1] && res[i-2] == res[i-3] {
					continue
				}
			}

			res = append(res, w)

		}
		fmt.Println(string(res))
		n -= 1
	}

}
