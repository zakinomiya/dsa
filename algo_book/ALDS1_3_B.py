from dataclasses import dataclass

@dataclass
class Task:
    name: str = ""
    remaining: int = 0

    def process(self, time):
        if self.remaining <= time:
            self.remaining = 0
        else:
            self.remaining -= time

    def isDone(self):
        return self.remaining == 0


class Queue:
    def __init__(self, length) -> None:
        # to differentiate full and empty, we will actually have length+1 space in the array
        self.q = [Task() for _ in range(length+1)]
        self.cap = length
        self.head = 0
        self.tail = 0

    def isFull(self) -> bool:
        return self.head == (self.tail + 1) % len(self.q)

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def enqueue(self, n):
        if self.isFull():
            return 

        self.q[self.tail] = n
        self.tail += 1
        self.tail %= len(self.q)

    def dequeue(self):
        if self.isEmpty():
            return None

        v = self.q[self.head]
        self.head += 1
        self.head %= len(self.q)

        return v


def main():
    q = Queue(5)
    q.enqueue(Task("p1", 150))
    q.enqueue(Task("p2", 80))
    q.enqueue(Task("p3", 200))
    q.enqueue(Task("p4", 350))
    q.enqueue(Task("p5", 20))

    total_time = 0
    while not q.isEmpty():
        task = q.dequeue()
        if task is None:
            continue

        t = task.remaining
        task.process(time=100)
        if not task.isDone():
            q.enqueue(task)
            total_time += 100
        else:
            total_time += t
            print(task.name, total_time)

if __name__ == "__main__":
    main()
