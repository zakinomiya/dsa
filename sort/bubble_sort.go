package sort

import "fmt"

type Order int

const (
	Asc Order = iota + 1
	Desc
)

func comp(a int, b int, order Order) bool {
  if order == Asc {
    return a > b
  } else {
    return a < b
  }
}

func bubbleSort(data []int, order Order) []int {
	for i := 0; i < len(data)-1; i++ {
		for j := 0; j < len(data)-i-1; j++ {
			if comp(data[j], data[j+1], order) {
				data[j], data[j+1] = data[j+1], data[j]
        fmt.Printf("%+v\n", data)
			}
		}
	}

	return data
}
