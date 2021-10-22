package sort

//func insert(data []int, v int) []int {
//	for i, d := range data {
//		if d >= v {
//      data = append(data, data[len(data)-1])
//			for j := len(data)-1; j > i; j-- {
//				data[j] = data[j - 1]
//			}
//			data[i] = v
//      return data
//		}
//	}
//
//  data = append(data, v)
//  return data
//}
//
//func insertionSort(data []int) []int {
//	sorted := make([]int, 0, len(data))
//
//  for _, v := range data {
//    sorted = insert(sorted, v)
//	}
//
//	return sorted
//}

func insertionSort(data []int) []int {
  // i is the last index of sorted part
	for i := 0; i < len(data)-2; i++ {
    current := data[i+1]
  // 1. if the last sorted item is bigger than the current item: the current item
  //    should be placed somewhere in the sorted part.
  // 2. else: just see it as already sorted and increment i
		if data[i] > current {
      // see where the current item should be placed from right to left
			for j := i; j > 0; j-- {
        // if an item which is smaller than or equal to the current found, then the current 
        // should be right next to that item. so insert the current there and shift items right by one
        if data[j] <= current {
          for k := j; k < i; k-- {
            data[k+1] = data[k]
          }
        }
			}
		}
	}
 
	return data
}