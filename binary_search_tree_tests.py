import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])
        
    def test_simple2(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertFalse(bst.search(11))
        
    def test_simple3(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(10))
        
    def test_simple4(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        bst.insert(11, 'more stuff')
        bst.insert(12, 'even more stuff')
        self.assertTrue(bst.search(12))
        
    def test_simple5(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        bst.insert(11, 'more stuff')
        bst.insert(12, 'even more stuff')
        bst.insert(9, 'gotta have more stuff')
        self.assertTrue(bst.search(9))
        
    def test_simple6(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(11))
        self.assertEqual(bst.find_min(), None)
        bst.insert(10, 'stuff')
        bst.insert(11, 'more stuff')
        bst.insert(12, 'even more stuff')
        bst.insert(9, 'gotta have more stuff')
        self.assertEqual(bst.find_min(), (9, 'gotta have more stuff'))
        
    def test_simple7(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(11))
        self.assertEqual(bst.find_max(), None)
        bst.insert(10, 'stuff')
        bst.insert(11, 'more stuff')
        bst.insert(12, 'even more stuff')
        bst.insert(9, 'gotta have more stuff')
        self.assertEqual(bst.find_max(), (12, 'even more stuff'))
        
    def test_simple8(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(11))
        self.assertEqual(bst.tree_height(), None)
        self.assertEqual(bst.level_order_list(), [])
        

if __name__ == '__main__': 
    unittest.main()
