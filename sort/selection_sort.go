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

func max(data []int) (int, int) {
	m := data[0]
	index := 0
	for i, v := range data {
		if m < v {
			m = v
			index = i
		}
	}
	return m, index
}

func selectionSort(data []int, order Order) []int {
  for i := range data {
    var m, ind int
    if order == Asc {
      m, ind = min(data[i:])
    } else {
      m, ind = max(data[i:])
    }
    data[ind+i] = data[i]
    data[i] = m
  }

	return data
}
