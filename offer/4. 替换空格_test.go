package offer

import "testing"

func TestSolution4(t *testing.T) {
	strs := []struct {
		in     string
		except string
	}{
		{"hello world", "hello%20world"},
		{" hello world", "%20hello%20world"},
		{"hello world ", "hello%20world%20"},
		{"hello  world", "hello%20%20world"},
		{"", ""},
		{" ", "%20"},
		{"    ", "%20%20%20%20"},
	}

	for _, v := range strs {
		actual := solution4(v.in)
		if actual != v.except {
			t.Error(actual, " but-> ", actual)
		}
	}
}

func solution4(str string) string {

	return str
}
