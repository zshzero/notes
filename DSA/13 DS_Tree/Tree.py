class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
        

class BinarySearchTree:
  def __init__(self, value = None):
    if not value:
      self.root = None
      return
    
    node = Node(value)
    self.root = node
    return     

  def insert(self, value):
    node = Node(value)
    if not self.root:
      self.root = node
      return True
    
    itr = self.root
    while itr:
      if itr.value == node.value:
        return False
      if itr.value > node.value:
        if not itr.left:
          itr.left = node
          return True
        itr = itr.left
      elif itr.value < node.value:
        if not itr.right:
          itr.right = node
          return True
        itr = itr.right

  def contains(self, value):
    itr = self.root
    while itr:
      if value < itr.value:
        itr = itr.left
        continue
      if value > itr.value:
        itr = itr.right
        continue
      return itr
    
    return None

bst = BinarySearchTree()
print(bst.contains(10))

bst.insert(50)
print(bst.contains(50).value)
bst.insert(40)
print(bst.contains(40).value)
bst.insert(60)
print(bst.contains(60).value)
bst.insert(30)
print(bst.contains(30).value)
bst.insert(70)
print(bst.contains(70).value)
