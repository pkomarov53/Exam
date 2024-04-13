class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)

    def swap_first_and_last(self):
        if self.size() >= 2:
            first_item = self.dequeue()
            last_item = self.items.pop()
            self.items.insert(0, last_item)
            self.items.append(first_item)


# Пример использования
queue = Queue()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(1)

print("Очередь до обмена:", queue.items)

queue.swap_first_and_last()

print("Очередь после обмена:", queue.items)
