class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self, value = None):
    if not value:
      self.root = None
    else:
      self.root = Node(value)

      self.right = None
      self.left = None

  def __r_insert(self, node, value):
    if node == None:
      return Node(value)
    if node.value == value:
      return False
    
    if node.value > value:
      node.left = self.__r_insert(node.left, value)
    elif node.value < value:
      node.right = self.__r_insert(node.right, value)
    return node

  def r_insert(self, value):
    if not self.root:
      self.root = Node(value)
      return True
    
    self.__r_insert(self.root, value)
    return True
  
  def traverse_bfs(self):
    print()
    print("-----------------------------")
    if not self.root:
      print("Empty BST")
      return 
    
    queue = [self.root]
    result = []
    
    while queue:
      node = queue.pop(0)
      result.append(node.value)
      if node.left: queue.append(node.left)
      if node.right: queue.append(node.right)
    
    print(result)
    print("-----------------------------")
    print()

  def traverse_dfs_preorder(self):
    def __traverse_dfs_preorder(node):
      if not node: return
      results.append(node.value)
      if node.left: __traverse_dfs_preorder(node.left)
      if node.right: __traverse_dfs_preorder(node.right)

    print()
    print("-----------------------------")

    results = []
    __traverse_dfs_preorder(self.root)

    print(results)
    print("-----------------------------")
    print()

  def traverse_dfs_postorder(self):
    def __traverse_dfs_postorder(node):
      if not node: return
      if node.left: __traverse_dfs_postorder(node.left)
      if node.right: __traverse_dfs_postorder(node.right)
      result.append(node.value)

    print()
    print("-----------------------------")
    
    result = []
    __traverse_dfs_postorder(self.root)

    print(result)
    print("-----------------------------")
    print()

  def traverse_dfs_inorder(self):
    def __traverse_dfs_inorder(node):
      if not node: return
      if node.left: __traverse_dfs_inorder(node.left)
      results.append(node.value)
      if node.right: __traverse_dfs_inorder(node.right)

    print()
    print("-----------------------------")

    results = []
    __traverse_dfs_inorder(self.root)

    print(results)
    print("-----------------------------")  
    print()

bst = Tree()
bst.traverse_bfs()
bst.r_insert(47)
bst.traverse_bfs()

bst.r_insert(76)
bst.traverse_bfs()

bst.r_insert(21)
bst.traverse_bfs()

bst.r_insert(18)
bst.r_insert(27)
bst.r_insert(52)
bst.r_insert(82)

bst.traverse_bfs()
bst.traverse_dfs_preorder()
bst.traverse_dfs_postorder()
bst.traverse_dfs_inorder()