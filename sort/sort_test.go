package sort

import (
	"reflect"
	"testing"
)

var arr = []int{9, 4, 2, 3, 1, 5, 8, 6, 7}
var ascSorted = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
var descSorted = []int{9, 8, 7, 6, 5, 4, 3, 2, 1}

func TestBubbleSort(t *testing.T) {

	t.Log("test case 1")
	if s := bubbleSort(arr, Asc); !reflect.DeepEqual(s, ascSorted) {
		t.Errorf("bubble sort failed. expected: %+v. actual: %+v", ascSorted, s)
	}

	t.Log("test case 2")
	if s := bubbleSort(arr, Desc); !reflect.DeepEqual(s, descSorted) {
		t.Errorf("bubble sort failed. expected: %+v. actual: %+v", descSorted, s)
	}

	t.Log("test case 3: already sorted array")
	if s := bubbleSort(ascSorted, Asc); !reflect.DeepEqual(s, ascSorted) {
		t.Errorf("bubble sort failed. expected: %+v. actual: %+v", ascSorted, s)
	}
}

func TestSelectionSort(t *testing.T) {
  t.Log("test case 1")
  if s := selectionSort(arr, Asc); !reflect.DeepEqual(s, ascSorted) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }

  t.Log("test case 2")
  if s := selectionSort(arr, Desc); !reflect.DeepEqual(s, descSorted) {
    t.Errorf("bubble sort failed. expected: %+v. actual: %+v", descSorted, s)
  }

  t.Log("test case 3: already sorted array")
  if s := selectionSort(ascSorted, Asc); !reflect.DeepEqual(s, ascSorted) {
    t.Errorf("sort failed. expected: %+v. actual: %+v", ascSorted, s)
  }
}
