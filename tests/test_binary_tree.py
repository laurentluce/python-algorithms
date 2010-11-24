import unittest
import binary_tree

class BinaryTreeTest(unittest.TestCase):
    
  def test_binary_tree(self):

    data = [10, 5, 15, 4, 7, 13, 17, 11, 14]
    # create 2 trees with the same content
    bt = binary_tree.BinaryTree()
    for i in data:
      bt.insert(i)

    bt2 = binary_tree.BinaryTree()
    for i in data:
      bt2.insert(i)

    # check if both trees are identical
    self.assertTrue(bt.compare_trees(bt2.get_root()))

    # check the content of the tree inorder
    t = []
    for d in bt.tree_data():
      t.append(d)
    self.assertEquals(t, [4, 5, 7, 10, 11, 13, 14, 15, 17])

    # test lookup
    node, parent = bt.lookup(9)
    self.assertTrue(node == None)
    node, parent = bt.lookup(11)
    self.assertTrue(node.data == 11)
    self.assertTrue(parent.data == 13)

    # delete a leaf node
    bt.delete(4)
    # check the content of the tree inorder
    t = []
    for d in bt.tree_data():
      t.append(d)
    self.assertEquals(t, [5, 7, 10, 11, 13, 14, 15, 17])

    # delete a node with 1 child
    bt.delete(5)
    # check the content of the tree inorder
    t = []
    for d in bt.tree_data():
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 13, 14, 15, 17])

    # delete a node with 2 childs
    bt.delete(13)
    # check the content of the tree inorder
    t = []
    for d in bt.tree_data():
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 14, 15, 17])

    # delete a node with 2 childs
    bt.delete(15)
    # check the content of the tree inorder
    t = []
    for d in bt.tree_data():
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 14, 17])

if __name__ == '__main__':
  unittest.main()

