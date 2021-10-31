package cache

import "testing"

func TestLRUCache(t *testing.T) {
	cache, _ := NewLRUCache(5)
	cache.Put(1, 1)
	cache.Put(2, 2)
	cache.Put(3, 3)
	cache.Put(4, 4)
	cache.Put(5, 5)
	if deleted := cache.Put(6, 6); deleted.data != 1 {
		t.Errorf("data with key 1 is cache and so should be removed, but given %+v\n", deleted.data)
	}

	if d := cache.Get(2); d.data != 2 {
		t.Errorf("expected 2 but got %s\n", d.data)
	}

	if deleted := cache.Put(7, 7); deleted.data != 3 {
		t.Errorf("data with key 3 is cache and so should be removed, but given %s\n", deleted.data)
	}
}

func TestLRUCache2(t *testing.T) {
	cache, _ := NewLRUCache2(5)
	cache.Put(1, 1)
	cache.Put(2, 2)
	cache.Put(3, 3)
	cache.Put(4, 4)
	cache.Put(5, 5)
	if deleted := cache.Put(6, 6); deleted.data != 1 {
		t.Errorf("data with key 1 is cache and so should be removed, but given %+v\n", deleted.data)
	}

	if d := cache.Get(2); d.data != 2 {
		t.Errorf("expected 2 but got %s\n", d.data)
	}

	if deleted := cache.Put(7, 7); deleted.data != 3 {
		t.Errorf("data with key 3 is cache and so should be removed, but given %s\n", deleted.data)
	}
}

