import unittest
import LCA
import pdb
from LCA import findLCA
from LCA import findPath 
from LCA import Node 


class TestLCA(unittest.TestCase):

	def testNodes(self): #Testing root value in the tree

		root = Node(1)
		self.assertEqual(1, root.key)

	def testFindLCA(self):

		root = Node(1)
		root.left = Node(2)
		root.right = Node(3)
		root.left.left = Node(4)
		root.left.right = Node(5)
		root.right.left = Node(6)
		root.right.right = Node(7)

		# test all nodes are None 
		#self.assertEqual(LCA.findLCA(None, None, None), -1)

		#test when root is euqal to node
		#root = Node(1)
		self.assertEqual(LCA.findLCA(root, 1, 1), 1)

		#test if n2 is not present
		self.assertEqual(LCA.findLCA(root, 2, None), -1)

		#test when node is value is not in tree
		self.assertEqual(LCA.findLCA(root, 2, 13), -1)

		#test LCA for different values
		self.assertEqual(findLCA(root, 3, 7), 3)
		self.assertEqual(findLCA(root, 4, 6), 1)
		self.assertEqual(findLCA(root, 2, 5), 2)
		self.assertEqual(findLCA(root, 3, 4), 1)






if __name__ == '__main__':
	unittest.main()
