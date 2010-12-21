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

  def insert(self, data):
    """
    Insert new node with data

    @param data node data object to insert
    """
    elif data < self.data:
      if self.left == None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right == None:
        self.right = Node(data)
      else:
        self.right.insert(data)

  def lookup(self, data, parent=None):
    """
    Lookup node containing data

    @param data node data object to look up
    @param parent node's parent
    @returns node and node's parent if found or None, None
    """
    if data < self.data:
      if self.left == None:
        return None, None
      return self.left.lookup(data, self)
    elif data > self.data:
      if self.right == None:
        return None, None
      return self.right.lookup(data, self)
    else:
      return self, parent

  def delete(self, data):
    """
    Delete node containing data

    @param data node's content to delete
    """
    # get node containing data
    node, parent = self.lookup(data)
    if node != None:
      children_count = self.children_count(node)
      if children_count == 0:
        # if node has no children, just remove it
        if self.which_child(parent, node) == 'left':
          parent.left = None
        else:
          parent.right = None
      elif children_count == 1:
        # if node has 1 child
        # replace node by its child
        if node.left:
          node.data = node.left.data
          node.left = None
        else:
          node.data = node.right.data
          node.right = None
      else:
        # if node has 2 children
        # find its successor
        parent = node
        successor = node.right
        while successor.left:
          parent = successor
          successor = successor.left
        # replace node data by its successor data
        node.data = successor.data
        # fix successor's parent node child
        if parent.left == successor:
          parent.left = successor.right
        else:
          parent.right = successor.right

  def compare_trees(self, node):
    """
    Compare 2 trees

    @param node tree to compare
    @returns True if the tree passed is identical to this tree
    """
    if node == None:
      return False
    if self.data != node.data:
      return False
    res = True
    if self.left == None:
      if node.left:
        return False
    else:
      res = self.left.compare_trees(node.left)
    if self.right == None:
      if node.right:
        return False
    else:
      res = self.right.compare_trees(node.right)
    return res
        
  def print_tree(self):
    """
    Print tree content inorder
    """
    if self.left:
      self.left.print_tree()
    print self.data,
    if self.right:
      self.right.print_tree()

  def tree_data(self):
    """
    Generator to get the tree nodes data
    """
    # we use a stack to traverse the tree in a non-recursive way
    stack = []
    node = self
    while stack or node: 
      if node:
        stack.append(node)
        node = node.left
      else: # we are returning so we pop the node and we yield it
        node = stack.pop()
        yield node.data
        node = node.right

  def which_child(self, parent, child):
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

  def children_count(self, node):
    """
    Return the number of children

    @param node node to get nb of children
    @returns number of children: 0, 1, 2
    """
    if node == None:
      return None
    cnt = 0
    if node.left:
      cnt += 1
    if node.right:
      cnt += 1
    return cnt



