class Node:
  """
  Tree node: left and right child + data which can be any object
  """
  def __init__(self, data):
    """
    Node constructor

    @param data node data object
    """
    self.left = None
    self.right = None
    self.data = data

class BinaryTree:
  """
  Binary tree: methods to manipulate a binary tree
  """
  def __init__(self):
    """
    Binary tree constructor
    """
    self.root = None

  def get_root(self):
    return self.root

def bt_insert(root, data):
  """
  Insert new node with data

  @param root tree root
  @param data node data object
  @returns inserted node
  """
  if root == None:
    root = Node(data)
  else:
    if data <= root.data:
      root.left = bt_insert(root.left, data)
    else:
      root.right = bt_insert(root.right, data)
  return root

def bt_lookup(root, data, parent=None):
  """
  Lookup node containing data

  @param root tree root
  @param data node data object
  @returns node and node's parent if found or None, None
  """
  if root == None:
    return None, None
  if data < root.data:
    return bt_lookup(root.left, data, root)
  elif data > root.data:
    return bt_lookup(root.right, data, root)
  else:
    return root, parent

def bt_compare_trees(t1, t2):
  """
  Compare 2 trees

  @param t1 tree 1
  @param t2 tree 2
  @returns True if the 2 trees are identical or False
  """
  if t1 == None and t2 == None:
    return True
  elif (t1 == None and t2 != None) or (t1 != None and t2 == None):
    return False
  else:
    return (t1.data == t2.data) \
        and bt_compare_trees(t1.left, t2.left) \
        and bt_compare_trees(t1.right, t2.right)

def bt_print_tree(root):
  """
  Print tree content in order

  @param root tree root node
  """
  if root == None:
    pass
  else:
    bt_print_tree(root.left)
    print root.data,
    bt_print_tree(root.right)

def bt_tree_data(node):
  """
  Generator to get the tree nodes data

  @param node tree root node
  """
  # we use a stack to traverse the tree in a non-recursive way
  stack = []
  while stack or node: 
    if node:
      stack.append(node)
      node = node.left
    else: # we are returning so we pop the node and we yield it
      node = stack.pop()
      yield node.data
      node = node.right

def bt_delete(root, data):
  """
  Delete node containing data

  @param root tree root node
  @param data node's content to delete
  """
  # get node containing data
  node, parent = bt_lookup(root, data)
  if node != None:
    childs_count = bt_childs_count(node)
    if childs_count == 0:
      # if node has no childs, just remove it
      if bt_which_child(parent, node) == 'left':
        parent.left = None
      else:
        parent.right = None
    elif childs_count == 1:
      # if node has 1 child
      # replace node by its child
      if node.left:
        node.data = node.left.data
        node.left = None
      else:
        node.data = node.right.data
        node.right = None
    else:
      # if node has 2 childs
      # find its successor
      successor = node.right
      while successor.left:
        successor = successor.left
      node.data = successor.data
      # if the successor has a child, replace it with its child
      # it can only be a right child at this point
      if successor.right:
        successor.data = successor.right.data
        successor.right = None
      else:
        node.right = None

def bt_which_child(parent, child):
  """
  Test if child is parent's left child or parent's right child

  @param parent parent node
  @param child parent's child node
  """
  if parent == None:
    return None
  if parent.left == child:
    return 'left'
  else:
    return 'right'

def bt_childs_count(node):
  """
  Return the number of childs

  @param node node to get nb of childs
  @returns number of childs: 0, 1, 2
  """
  if node == None:
    return None
  cnt = 0
  if node.left:
    cnt += 1
  if node.right:
    cnt += 1
  return cnt



