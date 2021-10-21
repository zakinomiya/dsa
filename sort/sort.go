package sort

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

