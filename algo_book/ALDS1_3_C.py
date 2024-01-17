from dataclasses import dataclass

from typing_extensions import Self

@dataclass
class Node:
    next: Self | None
    prev: Self | None
    key: int

@dataclass
class List: 
    head: Node | None = None
    tail: Node | None = None

    def insert(self, key: int):
        n = Node(key=key, prev=None, next=None)
        if self.head is None:
            self.head = n
            self.tail = n
        else: 
            n.prev = self.head
            self.head.next = n
            self.head = n

    def delete(self, key: int):
        if self.head is None:
            return None

        if self.head.key == key:
            self.deleteFirst()
            return

        current = self.head
        while current.prev is not None and current.key != key:
            current = current.prev

        if current.prev is not None:
            current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev

    def deleteFirst(self):
        if self.head is None:
            return 

        if self.head.prev is not None:
            self.head.prev.next = None
            self.head = self.head.prev
        else:
            self.head = None
            self.tail = None

    def deleteLast(self):
        if self.tail is None:
            return 

        if self.tail.next is not None:
            self.tail.next.prev = None
            self.tail = self.tail.next
        else:
            self.head = None
            self.tail = None

def print_items(l: List):
    print("items:")
    h = l.head
    while h is not None:
        print(h.key)
        h = h.prev

def main():
    l = List()

    l.insert(5)
    l.insert(2)
    l.insert(3)
    l.insert(1)
    l.delete(3)
    l.insert(6)
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
