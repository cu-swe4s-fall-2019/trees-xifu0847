import unittest
import binary_tree


class TestBinaryTree(unittest.TestCase):
    '''
    Unit test for binary_tree.py
    '''
    def test_init_node(self):
        node1 = binary_tree.Node('Cindy', 1)
        self.assertEqual(node1.key, 'Cindy')
        self.assertEqual(node1.value, 1)

        node2 = binary_tree.Node(2, 'Fu')
        self.assertEqual(node2.key, 2)
        self.assertEqual(node2.value, 'Fu')

    def test_insert(self):
        self.tree_root = None
        self.tree_root = binary_tree.insert(self.tree_root, 'Cindy', 1)
        self.tree_root = binary_tree.insert(self.tree_root, 'Fu', 2)
        self.tree_root = binary_tree.insert(self.tree_root, 'Computer', 5)
        self.tree_root = binary_tree.insert(self.tree_root, 'Science', 10)
        res = binary_tree.inorder(self.tree_root)
        self.assertEqual(res, [1, 5, 2, 10])

    def test_search(self):
        self.tree_root = None
        self.tree_root = binary_tree.insert(self.tree_root, 'Cindy', 1)
        self.tree_root = binary_tree.insert(self.tree_root, 'Fu', 2)
        self.tree_root = binary_tree.insert(self.tree_root, 'Computer', 5)
        self.tree_root = binary_tree.insert(self.tree_root, 'Science', 10)

        res1 = binary_tree.search(self.tree_root, 'Cindy')
        self.assertEqual(res1.value, 1)
        res2 = binary_tree.search(self.tree_root, 'Fu')
        self.assertEqual(res2.value, 2)
        res3 = binary_tree.search(self.tree_root, 'aldksfjlk')
        self.assertEqual(res3, None)


if __name__ == '__main__':
    unittest.main()
