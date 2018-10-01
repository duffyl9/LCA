import unittest
from LCA import findPath 
from LCA import __init__ 
from LCA import Node 
from LCA import findLCA
from LCA import findPath


class TestLCA(unittest.TestCase):

	def testNodes(self):

		root = Node(1)
		actualNodeOne = Node(root)
		self.assertEqual(1, root.key)


if __name__ == '__main__':
	unittest.main()
