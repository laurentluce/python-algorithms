import unittest
import algorithms.binary_tree as binary_tree

class BinaryTreeTest(unittest.TestCase):
    
  def test_binary_tree(self):

    data = [10, 5, 15, 4, 7, 13, 17, 11, 14]
    # create 2 trees with the same content
    root = binary_tree.Node(data[0])
    for i in data[1:]:
      root.insert(i)

    root2 = binary_tree.Node(data[0])
    for i in data[1:]:
      root2.insert(i)

    # check if both trees are identical
    self.assertTrue(root.compare_trees(root2))

    # check the content of the tree inorder
    t = []
    for d in root.tree_data():
      t.append(d)
    self.assertEquals(t, [4, 5, 7, 10, 11, 13, 14, 15, 17])

    # test lookup
    node, parent = root.lookup(9)
    self.assertTrue(node is None)
    # check if returned node and parent are correct
    node, parent = root.lookup(11)
    self.assertTrue(node.data == 11)
    self.assertTrue(parent.data == 13)

    # delete a leaf node
    root.delete(4)
    # check the content of the tree inorder
    t = []
    for d in root.tree_data():
      t.append(d)
    self.assertEquals(t, [5, 7, 10, 11, 13, 14, 15, 17])

    # delete a node with 1 child
    root.delete(5)
    # check the content of the tree inorder
    t = []
    for d in root.tree_data():
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 13, 14, 15, 17])

    # delete a node with 2 children
    root.delete(13)
    # check the content of the tree inorder
    t = []
    for d in root.tree_data():
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 14, 15, 17])

    # delete a node with 2 children
    root.delete(15)
    # check the content of the tree inorder
    t = []
    for d in root.tree_data():
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 14, 17])

    # check for root deletion
    root = binary_tree.Node(1)
    root.insert(2)
    root.insert(0)
    root.delete(1)
    self.assertEquals(root.data, 2)
    root.delete(2)
    self.assertEquals(root.data, 0)
    root.delete(0)
    self.assertEquals(root.data, None)
    root.insert(1)
    self.assertEquals(root.data, 1)
    self.assertEquals(root.left, None)
    self.assertEquals(root.right, None)


if __name__ == '__main__':
  unittest.main()

