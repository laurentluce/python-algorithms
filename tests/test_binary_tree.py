import unittest
import binary_tree

class BinaryTreeTest(unittest.TestCase):
    
  def test_binary_tree(self):

    data = [10, 5, 15, 4, 7, 13, 17, 11, 14]
    # create 2 trees with the same content
    bt = binary_tree.BinaryTree()
    root = binary_tree.bt_insert(bt.get_root(), data[0])
    for i in data[1:]:
      binary_tree.bt_insert(root, i)

    bt2 = binary_tree.BinaryTree()
    root2 = binary_tree.bt_insert(bt2.get_root(), data[0])
    for i in data[1:]:
      binary_tree.bt_insert(root2, i)

    # check if both trees are identical
    self.assertTrue(binary_tree.bt_compare_trees(root, root2))

    # check the content of the tree inorder
    t = []
    for d in binary_tree.bt_tree_data(root):
      t.append(d)
    self.assertEquals(t, [4, 5, 7, 10, 11, 13, 14, 15, 17])

    # test lookup
    node, parent = binary_tree.bt_lookup(root, 9)
    self.assertTrue(node == None)
    node, parent = binary_tree.bt_lookup(root, 11)
    self.assertTrue(node.data == 11)
    self.assertTrue(parent.data == 13)

    # delete a leaf node
    binary_tree.bt_delete(root, 4)
    # check the content of the tree inorder
    t = []
    for d in binary_tree.bt_tree_data(root):
      t.append(d)
    self.assertEquals(t, [5, 7, 10, 11, 13, 14, 15, 17])

    # delete a node with 1 child
    binary_tree.bt_delete(root, 5)
    # check the content of the tree inorder
    t = []
    for d in binary_tree.bt_tree_data(root):
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 13, 14, 15, 17])

    # delete a node with 2 childs
    binary_tree.bt_delete(root, 13)
    # check the content of the tree inorder
    t = []
    for d in binary_tree.bt_tree_data(root):
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 14, 15, 17])

    # delete a node with 2 childs
    binary_tree.bt_delete(root, 15)
    # check the content of the tree inorder
    t = []
    for d in binary_tree.bt_tree_data(root):
      t.append(d)
    self.assertEquals(t, [7, 10, 11, 14, 17])

if __name__ == '__main__':
  unittest.main()

