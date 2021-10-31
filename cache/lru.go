package cache

import (
	"time"
)

type Cache interface {
	Get(key int) *Data
	Put(key int, value interface{}) *Data
	Cap() int
	Size() int
}

type Data struct {
	data interface{}
	time time.Time
  next *Data
  key int
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

func NewLRUCache(cap int) *LRUCache {
	return &LRUCache{
		data: make(map[int]*Data, cap),
		cap:  cap,
	}
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
  delete (lru.data, key)
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
	data map[int]*Data
	cap  int

  head *Data
  tail *Data
}

func NewLRUCache2(cap int) *LRUCache2 {
	return &LRUCache2{
		data: make(map[int]*Data, cap),
		cap:  cap,
	}
}

func (lru *LRUCache2) Get(key int) *Data {
  p := lru.data[key]
  p.time = time.Now()
  return p
}

func (lru *LRUCache2) Put(key int, value interface{}) *Data {
  d := NewData(key, value)
  lru.head.next = d
  lru.head = d
  lru.data[key] = d

  if len(lru.data) > lru.cap {
    t := lru.tail
    lru.tail = lru.tail.next
    delete (lru.data, t.key)
    return t
  }

  return nil
}

