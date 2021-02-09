import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
        
    def test_queue2(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertTrue(q.is_full)
        
    def test_queue3(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        with self.assertRaises(IndexError):
          q.enqueue(5)
          
    def test_queue4(self):
        q = Queue(5)
        with self.assertRaises(IndexError):
          q.dequeue()
          
    def test_queue5(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        with self.assertRaises(IndexError):
          q.dequeue()

if __name__ == '__main__': 
    unittest.main()

