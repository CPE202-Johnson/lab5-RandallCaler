from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        if self.root is None:
          return True
        else:
          return False
        #pass

    def search(self, key): # returns True if key is in a node of the tree, else False
        return self.search_helper(self.root, key)
        #pass
        
    def search_helper(self, node, key):
        if node is None:
          return False
        if node.key == key:
          return True
        elif node.key > key and node.left is not None:
          return self.search_helper(node.left, key)
        elif node.key < key and node.right is not None:
          return self.search_helper(node.right, key)
        return False

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        self.insert_helper(self.root, key, data)
        #pass
        
    def insert_helper(self, node, key, data):
        newnode = TreeNode(key, data)
        if node is None:
          self.root = newnode
        elif node.key == key:
          node.data = data
        elif node.key > key:
          if node.left is None:
            node.left = newnode
          else:
            return self.insert_helper(node.left, key, data)
        elif node.key < key:
          if node.right is None:
            node.right = newnode
          else:
            return self.insert_helper(node.right, key, data)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty() is True:
          return None
        else:
          temp = self.root
          while temp.left is not None:
           temp = temp.left
          return (temp.key, temp.data)
        #pass

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty() is True:
          return None
        else:
          temp = self.root
          while temp.right is not None:
           temp = temp.right
          return (temp.key, temp.data)
        #pass

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty() is True:
          return None
        else:
          return self.tree_height_helper(self.root)-1
        #pass
        
    def tree_height_helper(self, node):
          if node is None:
            return 0
          else:
            left = self.tree_height_helper(node.left)
            right = self.tree_height_helper(node.right)
            return 1 + max(left, right)

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        return self.inorder_list_helper(self.root, [])
        #pass
        
    def inorder_list_helper(self, node, lst):
        if node is not None:
          self.inorder_list_helper(node.left, lst)
          lst.append(node.key)
          self.inorder_list_helper(node.right, lst)
        return lst 

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.preorder_list_helper(self.root, [])
        #pass
        
    def preorder_list_helper(self, node, lst):
        if node is not None:
          lst.append(node.key)
          self.preorder_list_helper(node.left, lst)
          self.preorder_list_helper(node.right, lst)
        return lst
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        lst = []
        q.enqueue(self.root)
        while q.size() > 0:
          temp = q.dequeue()
          lst.append(temp.key)
          if temp.left is not None:
            q.enqueue(temp.left)
          if temp.right is not None:
            q.enqueue(temp.right)
        return lst
        #pass
        

