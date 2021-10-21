package sort

func bubbleSort(data []int, order Order) []int {
	for i := 0; i < len(data)-1; i++ {
		for j := 0; j < len(data)-i-1; j++ {
			if comp(data[j], data[j+1], order) {
				data[j], data[j+1] = data[j+1], data[j]
			}
		}
	}

	return data
}
