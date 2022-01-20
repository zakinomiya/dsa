package sort

import "os"

func toHeap(data []int, lo int, hi int) []int {
	if len(data) == 0 {
		return data
	}

	k := hi/2 - 1
	for k >= lo {
		n := k*2 + 1
		if n >= hi {
			k--
			continue
		}

		bigger := n
		if n+1 <= hi && data[n+1] > data[n] {
			bigger = n + 1
		}

		if data[bigger] > data[k] {
			data[k], data[bigger] = data[bigger], data[k]
			if bigger%2 == 0 {
				k = bigger - 1
			} else {
				k = bigger
			}
			continue
		}

		k--
	}

	return data
}

func heapSort(data []int) []int {
	data = toHeap(data, 0, len(data)-1)

	for i := 0; i < len(data); i++ {
		data[0], data[len(data)-1-i] = data[len(data)-1-i], data[0]
		data = toHeap(data, 0, len(data)-1-(i+1))
	}

	return data
}
