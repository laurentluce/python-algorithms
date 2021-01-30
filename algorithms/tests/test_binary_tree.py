import copy
import unittest

import algorithms.binary_tree as binary_tree


class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.root_single_node = binary_tree.Node(None)
        self.root = binary_tree.Node(10)
        self.root.left = binary_tree.Node(5)
        self.root.left.left = binary_tree.Node(3)
        self.root.left.right = binary_tree.Node(7)
        self.root.right = binary_tree.Node(15)
        self.root.right.left = binary_tree.Node(12)
        self.root.right.left.left = binary_tree.Node(11)
        self.root.right.right = binary_tree.Node(20)
        self.root_copy = copy.deepcopy(self.root)

    def test_insert(self):
        root = self.root_single_node

        root.insert(10)
        self.assertEqual(root.data, 10)

        root.insert(5)
        self.assertEqual(root.left.data, 5)

        root.insert(15)
        self.assertEqual(root.right.data, 15)

        root.insert(8)
        self.assertEqual(root.left.right.data, 8)

        root.insert(2)
        self.assertEqual(root.left.left.data, 2)

        root.insert(12)
        self.assertEqual(root.right.left.data, 12)

        root.insert(17)
        self.assertEqual(root.right.right.data, 17)

    def test_lookup(self):
        node, parent = self.root.lookup(0)
        self.assertIsNone(parent)
        self.assertIsNone(node)

        node, parent = self.root.lookup(13)
        self.assertIsNone(parent)
        self.assertIsNone(node)

        node, parent = self.root.lookup(7)
        self.assertIs(node, self.root.left.right)
        self.assertIs(parent, self.root.left)

    def test_delete_root_no_child(self):
        self.root_single_node.data = 7
        self.root_single_node.delete(7)
        self.assertIsNone(self.root_single_node.data)

    def test_delete_root_one_child(self):
        self.root_single_node.data = 7
        self.root_single_node.insert(3)
        self.root_single_node.delete(7)
        self.assertEqual(self.root_single_node.data, 3)

    def test_delete_one_child_left(self):
        self.root.delete(12)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_one_child_right(self):
        self.root.insert(25)
        self.root.delete(20)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 25)

    def test_delete_right_leaf(self):
        self.root.delete(7)
        self.assertIsNone(self.root.left.right)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_left_leaf(self):
        self.root.delete(3)
        self.assertIsNone(self.root.left.left)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_right_node_two_childs(self):
        self.root.delete(15)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.right.data, 20)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)

    def test_delete_left_node_two_childs(self):
        self.root.delete(5)
        self.assertEqual(self.root.left.data, 7)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.left.left.data, 11)
        self.assertEqual(self.root.right.right.data, 20)

    def test_delete_root_two_childs(self):
        self.root.delete(10)
        self.assertEqual(self.root.left.data, 5)
        self.assertEqual(self.root.left.left.data, 3)
        self.assertEqual(self.root.left.right.data, 7)
        self.assertEqual(self.root.data, 11)
        self.assertEqual(self.root.right.data, 15)
        self.assertEqual(self.root.right.left.data, 12)
        self.assertEqual(self.root.right.right.data, 20)

    def test_compare_trees_left_leaf_missing(self):
        self.root_copy.delete(11)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_right_leaf_missing(self):
        self.root_copy.delete(20)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_diff_value(self):
        self.root_copy.left.data = 16
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_extra_right_leaf(self):
        self.root_copy.insert(25)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_compare_trees_extra_left_leaf(self):
        self.root_copy.insert(18)
        self.assertFalse(self.root.compare_trees(self.root_copy))

    def test_print_tree(self):
        self.root.print_tree()

    def test_tree_data(self):
        self.assertEqual([e for e in self.root.tree_data()],
                         [3, 5, 7, 10, 11, 12, 15, 20])

if __name__ == '__main__':
    unittest.main()
