import unittest
import dag
from dag import findLCA
from dag import findPathsTo
from dag import pathTo
from dag import Node

class test_dag(unittest.TestCase):

    def testNodes(self): #Testing root value in the tree

        root = Node(1)
        self.assertEqual(1, root.key)

    def testfindLCA(self):

        root = Node(1)
        root.children.append(dag.Node(2)) 
        root.children.append(dag.Node(3))
        root.children[0].children.append(dag.Node(4))
        root.children[0].children.append(dag.Node(5))
        root.children[1].children.append(dag.Node(6))
        root.children[1].children.append(dag.Node(7)) 

        # test all nodes are None 
        self.assertEqual(dag.findLCA(None, None, None), None)

        #test when root is euqal to node
        self.assertEqual(dag.findLCA(root, 1, 1), 1)

        #test if n1 is not present
        self.assertEqual(dag.findLCA(root, None, 2), None)

        #test if n2 is not present
        self.assertEqual(dag.findLCA(root, 2, None), None)

        #test when node is value is not in tree
        self.assertEqual(dag.findLCA(root, 2, 13), None)

        #test dag for different values
        self.assertEqual(dag.findLCA(root, 3, 7), 3)
        self.assertEqual(dag.findLCA(root, 4, 6), 1)
        self.assertEqual(dag.findLCA(root, 2, 5), 2) 
        self.assertEqual(dag.findLCA(root, 3, 4), 1)

    def test_findLCA_v2(self):
        #Test 1: test all values equal None
        self.assertEqual(dag.findLCA(None, None, None), None)

        #Test 2: test when both node are root
        root = dag.Node(1)
        self.assertEqual(dag.findLCA(root, 1, 1), 1)

        #Test 3: test when a value is not in tree
        self.assertEqual(dag.findLCA(root, 50, 51), None)

        #Test 4: Test dag with 7 nodes
        root.children.append(dag.Node(2)) 
        root.children.append(dag.Node(3))
        root.children[0].children.append(dag.Node(4))
        root.children[0].children.append(dag.Node(5))
        root.children[1].children.append(dag.Node(6))
        root.children[1].children[0].children.append(dag.Node(5))
        root.children[1].children[0].children.append(dag.Node(7))

    
        self.assertEqual(dag.findLCA(root, 4, 5), 2)

        #Test 5: dag 4-6
        self.assertEqual(dag.findLCA(root, 4, 6), 1)

        #Test 6: dag 3-4
        self.assertEqual(dag.findLCA(root, 3, 4), 1)

        #Test 7: dag 2-4
        self.assertEqual(dag.findLCA(root, 2, 4), 2)

        #Test 8: nodes at different heights
        self.assertAlmostEqual(dag.findLCA(root, 2, 6), 1)

        #self.assertAlmostEqual(dag.findLCA(root, 6, 8), 3)
        self.assertEqual(dag.findLCA(root, 6, 7), 6)


    def test_pathTo(self):

        #Graph with 7 nodes
        root = dag.Node(1)
        root.children.append(dag.Node(2)) 
        root.children.append(dag.Node(3))
        root.children[0].children.append(dag.Node(4))
        root.children[0].children.append(dag.Node(5))
        root.children[1].children.append(dag.Node(6))
        root.children[1].children[0].children.append(dag.Node(5))
        root.children[1].children[0].children.append(dag.Node(7))

        #Test 1: Test when root is None
        self.assertEqual(dag.pathTo(None, 2, 3), False)

        #Test 2: Test all values are None
        self.assertEqual(dag.pathTo(None, None, None), False)

        #Test 3: test path to root
        self.assertEqual(dag.pathTo(root, [], 1), True)

        #Test 4: test for key not in tree
        self.assertEqual(dag.pathTo(root, [], 25), False)

        #Test 4: path to 7
        self.assertEqual(dag.pathTo(root, [], 7), True)

        #Test 6: path to 6
        self.assertEqual(dag.pathTo(root, [], 6), True)
        
        #Test 7: path to 5
        self.assertEqual(dag.pathTo(root, [], 5), True)

        #Test 8: path to 4
        self.assertEqual(dag.pathTo(root, [], 4), True)

        #Test 9: path to 3
        self.assertEqual(dag.pathTo(root, [], 3), True)

        #Test 10: path to 2
        self.assertEqual(dag.pathTo(root, [], 2), True)


    def test_findPathsTo(self):

        #new Graph
        root = dag.Node(1)
        root.children.append(dag.Node(2)) 
        root.children.append(dag.Node(3))
        root.children[0].children.append(dag.Node(4))
        root.children[1].children.append(dag.Node(6))
        root.children[1].children[0].children.append(dag.Node(5))
        root.children[1].children[0].children.append(dag.Node(7))

        #Test 1: test when root is equal None
        self.assertEqual(dag.findPathsTo(None, 2), [])

        #Test 2: test when key is None
        self.assertEqual(dag.findPathsTo(root, None), [])

        #Test 3: test when all keys are None
        self.assertEqual(dag.findPathsTo(None, None), [])

        #Test 4: test path to root
        self.assertEqual(dag.findPathsTo(root, 1), [[1]])

        #Test 5: test for key not in tree
        self.assertEqual(dag.findPathsTo(root, 25), [])

        #Test 6: paths to 7
        self.assertEqual(dag.findPathsTo(root, 7), [[1,3,6,7]])

        #Test 7: path to 5
        self.assertEqual(dag.findPathsTo(root, 5), [[1,3,6,5]])
        
        #Test 8: path to 4
        self.assertEqual(dag.findPathsTo(root, 4), [[1,2,4]])

        #Test 9: test for more than one path
        root.children[0].children[0].children.append(dag.Node(5))
        self.assertEqual(dag.findPathsTo(root, 5), [[1,2,4,5],[1,3,6,5]])



        

if(__name__ == '__main__'):
    unittest.main()