package sort

func min(data []int) (int, int) {
	m := data[0]
	index := 0
	for i, v := range data {
		if m > v {
			m = v
			index = i
		}
	}
	return m, index
}

func selectionSort(data []int) []int {
  for i := range data {
    m, ind := min(data[i:])
    data[ind+i] = data[i]
    data[i] = m
  }

	return data
}
