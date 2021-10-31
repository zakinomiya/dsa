package main

import "time"

type Cache interface {
  Get(key int) *Data
  Put(key int, value interface{}) *Data
  Cap() int
  Size() int
} 

type Data struct {
  data interface{}
  time time.Time
}

func NewData(data interface{}) *Data{
  return &Data{
    data: data,
    time: time.Now(),
  }

}


// LRUCache impklements least recently used cache
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
  return lru.Size() >= lru.Cap()
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
    if m.Before(v.time) {
      m = v.time
      key = k 
    }
  }

  defer delete(lru.data, key)
  return lru.data[key]
}

func (lru *LRUCache) updateUsedTime(key int) {
  lru.data[key].time = time.Now()
}

func (lru *LRUCache) Put(key int, value interface{}) *Data {
  lru.data[key] = NewData(value)
  if lru.isFull() {
    return lru.removeLRU()
  }

  return nil
}

func (lru *LRUCache) Get(key int)  *Data {
  lru.updateUsedTime(key)
  return lru.data[key]
}
