package sort

func merge(a []int, b []int) []int {
  if len(a) == 0 || len(b) == 0 {
    return append(a, b...)
  }

	n := len(a) + len(b)
	d := make([]int, n)
	acnt, bcnt := 0, 0

	for i := 0; i < n; i++ {
    if len(a) == acnt {
			d[i] = b[bcnt]
			bcnt++
      continue
    } else if len(b) == bcnt {
			d[i] = a[acnt]
			acnt++
      continue
    }

		if a[acnt] < b[bcnt] {
			d[i] = a[acnt]
			acnt++
		} else {
			d[i] = b[bcnt]
			bcnt++
		}
	}

	return d
}

func mergeSort(data []int) []int {
	if len(data) > 1 {
		return merge(mergeSort(data[:len(data)/2]), mergeSort(data[len(data)/2:]))
	}

  if len(data) <= 1 {
    return data
  } 

  if data[0] > data[1] {
    data[0], data[1] = data[1], data[0]
  }

  return data
}
