class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self, value = None):
    if not value:
      self.root = None
      return
    
    self.root = Node(value)
    return
  
  def r_insert(self, value):
    if not self.root:
      self.root = Node(value)
      return True
    
    self.__r_insert(self.root, value)
    return True 
  
  def __r_insert(self, node, value):  
    if node == None:
      return Node(value)
    if node.value < value:
      node.right = self.__r_insert(node.right, value)
    if node.value > value:
      node.left = self.__r_insert(node.left, value)
    # if node.value == value:
    #   return node
    return node
  
  def r_delete(self, value):
    return self.__r_delete(self.root, value)

  def __r_delete(self, node, value):
    if node == None:
      return None
    if node.value > value:
      node.left = self.__r_delete(node.left, value)
    elif node.value < value:
      node.right = self.__r_delete(node.right, value)
    else:
      if not node.left and not node.right:
        return None
      elif not node.left:
        node = node.right
      elif not node.right:
        node = node.left
      else:
        min_value_node = self.__min_value(node.right)
        node.value = min_value_node.value
        node.right = self.__r_delete(node.right, min_value_node.value)
    return node
  
  def __min_value(self, node):
    while node.left:
      node = node.left
    return node

  def r_contains(self, value):
    return self.__r_contains(self.root, value)
  
  def __r_contains(self, node, value):
    if not node:
      return False
    if node.value == value:
      return True
    if node.value < value:
      return self.__r_contains(node.right, value)
    if node.value > value:
      return self.__r_contains(node.left, value)
        
bst = BST()
bst.r_insert(50)
print(bst.r_contains(50))
print(bst.r_contains(10))

bst.r_insert(40)
print(bst.r_contains(40))

bst.r_insert(60)
print(bst.r_contains(60))

print("Root - ", bst.root.value)
print("Root's left - ", bst.root.left.value)
print("Root's right - ",bst.root.right.value)
print()
bst.r_delete(50)
print("Root - ", bst.root.value)
print("Root's left - ", bst.root.left.value)
print("Root's right - ",bst.root.right)