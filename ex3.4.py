import threading
import random
import time
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()
        self._not_full = threading.Condition(self._lock)
        self._not_empty = threading.Condition(self._lock)

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if (self.tail + 1) % self.size == self.head:
                # Queue is full, wait for a signal that the queue is not full
                self._not_full.wait(1)
            else:
                # Queue is not full, insert element
                if self.head == -1:
                    self.head = 0
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                self._not_empty.notify()
                self.unlock()
                return

            self.unlock()

    def dequeue(self):
        while True:
            self.lock()
            if self.head == -1:
                # Queue is empty, wait for a signal that the queue is not empty
                self._not_empty.wait(1)
            else:
                # Queue is not empty, remove element
                data = self.queue[self.head]
                if self.head == self.tail:
                    self.head = self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self._not_full.notify()
                self.unlock()
                return data

            self.unlock()

def producer():
    while True:
        # Implement producer function
        num = random.randint(1, 10)
        time.sleep(num)
        q.lock()
        q.enqueue(num)
        q.unlock()
        

def consumer():
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)

        # Wait for the generated number of seconds
        time.sleep(num)

        # Dequeue a number from the queue and print it
        q.lock()
        data = q.dequeue()
        q.unlock()
        if data is not None:
            print(f"Consumed {data}")

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
