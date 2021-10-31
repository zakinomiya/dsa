package cache

import (
	"errors"
	"time"
)

type Cache interface {
	Get(key int) *Data
	Put(key int, value interface{}) *Data
}

type Data struct {
	data interface{}
	time time.Time
}

func NewData(key int, data interface{}) *Data {
	return &Data{
		data: data,
		time: time.Now(),
	}
}

// ============================================
// LRUCache implements least recently used cache
// ============================================
type LRUCache struct {
	data map[int]*Data
	cap  int
}

func NewLRUCache(cap int) (*LRUCache, error) {
  if cap < 1 {
    return nil, errors.New("cap must be greater than 0")
  }

	return &LRUCache{
		data: make(map[int]*Data, cap),
		cap:  cap,
	}, nil
}

func (lru *LRUCache) isFull() bool {
	return lru.Size() > lru.Cap()
}

func (lru *LRUCache) Cap() int {
	return lru.cap
}

func (lru *LRUCache) Size() int {
	return len(lru.data)
}

// removeLRU removes least recently used elements from the cache
// this takes O(n) as map is not ordered so it takes n times compariosions to find lru element
func (lru *LRUCache) removeLRU() *Data {
	var key int
	m := time.Now()
	for k, v := range lru.data {
		if v.time.Before(m) {
			m = v.time
			key = k
		}
	}

	d := lru.data[key]
	delete(lru.data, key)
	return d
}

func (lru *LRUCache) updateUsedTime(key int) {
	lru.data[key].time = time.Now()
}

func (lru *LRUCache) Put(key int, value interface{}) *Data {
	lru.data[key] = NewData(key, value)
	if lru.isFull() {
		return lru.removeLRU()
	}

	return nil
}

func (lru *LRUCache) Get(key int) *Data {
	lru.updateUsedTime(key)
	return lru.data[key]
}

// ============================================
// LRUCache2 implements least recently used cache but improved put time of O(1)
// ============================================
type LRUCache2 struct {
	data map[int]*DoubleLinkedData
	cap  int

	head *DoubleLinkedData
	tail *DoubleLinkedData
}

type DoubleLinkedData struct {
	data interface{}
	time time.Time

	next *DoubleLinkedData
	prev *DoubleLinkedData
	key  int
}

func NewDoubleLinkedData(key int, value interface{}, next *DoubleLinkedData, prev *DoubleLinkedData) *DoubleLinkedData {
  d := &DoubleLinkedData{
		data: value,
		time: time.Now(),
		next: next,
		prev: prev,
		key:  key,
	}

  if prev != nil {
    prev.next = d
  }

  if next != nil {
    next.prev = d
  }

  return d
}

func NewLRUCache2(cap int) (*LRUCache2, error) {
  if cap < 1 {
    return nil, errors.New("cap must be greater than 0")
  }

	return &LRUCache2{
		data: make(map[int]*DoubleLinkedData, cap),
		cap:  cap,
	}, nil
}

func (lru *LRUCache2) Get(key int) *DoubleLinkedData {
	d := lru.data[key]
  if d == nil {
    return nil 
  }

	d.time = time.Now()
  if len(lru.data) == 1 {
    return d
  }

  if lru.tail == d && d.next != nil {
    lru.tail = d.next
  }

  if d.next != nil {
    d.next.prev = d.prev
  }
  if d.prev != nil {
    d.prev.next = d.next
  } 

  d.next = nil
  lru.head = d
	return d
}

func (lru *LRUCache2) Put(key int, value interface{}) *DoubleLinkedData {
	d := NewDoubleLinkedData(key, value, nil, lru.head)
	lru.head = d
  if lru.tail == nil {
    lru.tail = d
  }

	lru.data[key] = d
	if len(lru.data) > lru.cap {
		t := lru.tail
		lru.tail = lru.tail.next
    t.next = nil
    t.prev = nil
		delete(lru.data, t.key)
		return t
	}

	return nil
}
