class Queue:

    def __init__(self):
        self.queue_items = []

    # add item
    def enQueue(self, item):
        self.queue_items.append(item)

    # delete item
    def deQueue(self):
        total_len = len(self.queue_items)

        if (total_len < 1):
            print("Queue is empty!")
            return False

        else:
            result = self.queue_items[0]
            del self.queue_items[0]
            return result

    # check Queue
    def isEmpty(self):
        return not self.queue_items

    def printQueue(self):
        print(self.queue_items)


que = Queue()

print(que.isEmpty())
que.enQueue(1)
que.enQueue(3)
que.enQueue(5)
que.enQueue(7)
que.printQueue()
print(que.deQueue())
print(que.deQueue())
que.printQueue()
print(que.isEmpty())