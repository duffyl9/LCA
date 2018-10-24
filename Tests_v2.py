import unittest
import dag

class test_dag(unittest.TestCase):

    def test_findLCA(self):
        #Test 1: test all values equal None
        self.assertEqual(dag.findLCA(None, None, None), None)

        #Test 2: test when both node are root
        root = dag.Node(1)
        self.assertEqual(dag.findLCA(root, 1, 1), 1)

        #Test 3: test when a value is not in tree
        self.assertEqual(dag.findLCA(root, 50, 51), None)

        #Test 4: Test DAG with 7 nodes
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

        

if(__name__ == '__main__'):
    unittest.main()