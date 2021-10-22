package sort

import (
	"reflect"
	"testing"
)

var arr = []int{9, 4, 2, 3, 1, 5, 8, 6, 7}
var ascSorted = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
var descSorted = []int{9, 8, 7, 6, 5, 4, 3, 2, 1}
var empty = make([]int, 0)

func TestBubbleSort(t *testing.T) {

  t.Log("test case 1: asc")
	if s := bubbleSort(arr); !reflect.DeepEqual(s, ascSorted) {
		t.Errorf("bubble sort failed. expected: %+v. actual: %+v", ascSorted, s)
	}

  t.Log("test case 2: empty")
  if s := bubbleSort(empty); !reflect.DeepEqual(s, empty) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }
}

func TestSelectionSort(t *testing.T) {
  t.Log("test case 1: asc")
  if s := selectionSort(arr); !reflect.DeepEqual(s, ascSorted) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }

  t.Log("test case 2: empty")
  if s := selectionSort(empty); !reflect.DeepEqual(s, empty) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }
}

func TestInsetionSort(t *testing.T) {
  t.Log("test case 1: asc")
  if s := insertionSort(arr); !reflect.DeepEqual(s, ascSorted) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }

  t.Log("test case 2: empty")
  if s := insertionSort(empty); !reflect.DeepEqual(s, empty) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }
}

func TestShellSort(t *testing.T) {
  t.Log("test case 1: asc")
  if s := shellSort(arr); !reflect.DeepEqual(s, ascSorted) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }

  t.Log("test case 2: empty")
  if s := shellSort(empty); !reflect.DeepEqual(s, empty) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }
}

func TestMergeSort(t *testing.T) {
  data := []int{1}
  t.Logf("f: %+v. s: %+v \n", data[:len(data)/2], data[len(data)/2:])


  t.Log("test case 1: asc")
  if s := mergeSort(arr); !reflect.DeepEqual(s, ascSorted) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }

  t.Log("test case 2: empty")
  if s := mergeSort(empty); !reflect.DeepEqual(s, empty) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }
}
