import unittest
from LCA import findPath 
from LCA import __init__ 
from LCA import Node 

class TestLCA(unittest.TestCase):


# This code is to check that the testing works/ passes to start
	def testNodes(self):
		root = Node(self)
		expectedNodeOne = 1
		actualNodeOne = Node(root)
		#self.assertEqual(expectedNodeOne, actualNodeOne)
		#root.assertEqual(root.left, 2)
		#root.assertEqual(root.left, 2)
		#root.assertEqual(root.right, 3)
		#root.assertEqual(root.left.left, 4)
		#root.assertEqual(root.left.right, 5)
		#root.assertEqual(root.right.left, 6)
		#root.assertEqual(root.right.right, 7)
if __name__ == '__main__':
	unittest.main()
