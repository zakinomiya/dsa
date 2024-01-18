from dataclasses import dataclass, field

from typing_extensions import Self

@dataclass
class Node:
    next: Self = field(init=False)
    prev: Self = field(init=False)
    key: int 

    def __post_init__(self):
        self.next = self
        self.prev = self

    @staticmethod
    def nil_node(): 
        n = Node(key=-1) 
        n.next = n
        n.prev = n
        return n

    @staticmethod
    def new_node(next, prev, key: int):
        n = Node(key=key)
        n.next = next
        n.prev = prev
        return n

    def is_nil(self) -> bool:
        return self.key == -1

@dataclass
class List: 
    sentinel: Node

    def head(self) -> Node | None:
        return self.sentinel.next

    def tail(self) -> Node | None:
        return self.sentinel.prev

    @staticmethod
    def new_list():
        nil = Node.nil_node()
        return List(sentinel=nil)

    def search(self, key: int):
        cur = self.sentinel.next
        while cur.is_nil() == False and cur.key != key :
            cur = cur.next

        return None if cur.is_nil() else cur


    def insert(self, key: int):
        if self.sentinel.next.is_nil():
            n = Node.new_node(next=self.sentinel, prev=self.sentinel, key=key)
            self.sentinel.next = n
            self.sentinel.prev = n
        else: 
            n = Node.new_node(next=self.sentinel.next, prev=self.sentinel, key=key)
            self.sentinel.next.prev = n
            self.sentinel.next = n

    def delete(self, key: int):
        n = self.search(key)
        if n is None:
            return 

        n.prev.next = n.next
        n.next.prev = n.prev

    def deleteFirst(self):
        first = self.sentinel.next
        if first.is_nil() == False:
            first.next.prev = self.sentinel
            self.sentinel.next = first.next

    def deleteLast(self):
        last = self.sentinel.prev
        if last.is_nil() == False:
            self.sentinel.prev = last.prev
            last.prev.next = self.sentinel

def print_items(l: List):
    print("items:")
    h = l.sentinel.next
    while h.is_nil() == False:
        print(h.key)
        h = h.next

def main():
    l = List.new_list()

    l.insert(5)
    l.insert(2)
    l.insert(3)
    l.insert(1)
    l.insert(6)
    l.delete(3)
    l.delete(2)
    print_items(l)
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    l.deleteLast()
    print_items(l)

if __name__ == "__main__":
    main()
