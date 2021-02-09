
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.head = 0
        self.tail = 0
        #pass


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
          return True
        else:
          return False
        #pass


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
          return True
        else:
          return False
        #pass


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full() is True:
          raise IndexError
        else:
          self.items[self.tail] = item
          self.tail += 1
        if self.tail > self.capacity-1:
          self.tail = 0
        self.num_items += 1
        #pass


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty() is True:
          raise IndexError
        else:
          self.head += 1
          temp = self.head-1
          if self.head > self.capacity-1:
            self.head = 0
          self.num_items -= 1
          return self.items[temp]
        #pass


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
        #pass


