from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.head = None
        self.tail = None
        self.storage = []

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

    def len(self):
        return self.size
