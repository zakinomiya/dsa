package cache

import "testing"

func TestLRUCache(t *testing.T) {
	lru := NewLRUCache(5)

	lru.Put(1, 1)
	lru.Put(2, 2)
	lru.Put(3, 3)
	lru.Put(4, 4)
	lru.Put(5, 5)
	if deleted := lru.Put(6, 6); deleted.data != 1 {
		t.Errorf("data with key 1 is lru and so should be removed, but given %+v\n", deleted.data)
	}

	if d := lru.Get(2); d.data != 2 {
		t.Errorf("expected 2 but got %s\n", d.data)
	}

	if deleted := lru.Put(7, 7); deleted.data != 3 {
		t.Errorf("data with key 3 is lru and so should be removed, but given %s\n", deleted.data)
	}
}
