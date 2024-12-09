class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self, value = None):
    if not value:  
      self.head, self.tail = None, None
      return
    
    node = Node(value)
    self.tail, self.head = node, node

  def append(self, value):
    node = Node(value)
    # Edge Case: 1
    if not self.head:
      self.tail, self.head = node, node
      return True

    self.tail.next = node
    node.prev = self.tail
    self.tail = node
    return True

  def pop(self):
    # Edge Case: 1
    if not self.head:
      return None

    ele = self.tail

    # Edge Case: 2
    if self.head is self.tail:     
      self.head, self.tail = None, None
      return ele

    self.tail = ele.prev 
    self.tail.next = None
    ele.prev = None
    return ele
  
  def prepend(self, value):
    node = Node(value)
    # Edge Case: 1
    if not self.head:
      self.head, self.tail = node, node
      return True
    
    node.next = self.head
    self.head.prev = node
    self.head = node
    return True
  
  def pop_first(self):
    # Edge Case: 1
    if not self.head:
      return None
    
    ele = self.head
    # Edge Case: 2
    if self.head is self.tail:
      self.head, self.tail = None, None
      return ele

    self.head = ele.next
    self.head.prev = None
    ele.next = None
    return ele
  
  def get_node(self, index):
    # Edge Case: 1
    if index < 0:
      print("Negative Index")
      return None
     
    itr = self.head
    while index > 0 and itr:
      itr = itr.next
      index -= 1
    # Edge Case: 2
    if not itr:
      print("Out of Bound Exception")
      return None
    
    return itr
  
  def set_node(self, index, value):
    node = self.get_node(index)
    # Edge Case: 1
    if not node:
      return False
    
    node.value = value
    return True
  
  def insert(self, index, value):
    # Edge Case: 1
    if not self.head or index == 0:
      return self.prepend(value)
    
    after = self.get_node(index)
    # Edge Case: 2
    if not after:
      return False
    
    new_node = Node(value)
    before = after.prev

    new_node.prev, new_node.next = before, after
    before.next, after.prev = new_node, new_node
    return True
  
  def remove(self, index):
    # Edge Case: 1
    if not self.head or index == 0:
      return self.pop_first() 
    
    node = self.get_node(index)
    # Edge Case: 2
    if not node:
      return None
    
    # Edge Case: 3
    if node is self.tail:
      return self.pop()
    
    before = node.prev
    after = node.next

    before.next, after.prev = after, before
    node.next, node.prev = None, None
    return node
  
  def print(self):
    itr = self.head
    print()
    print("-----------------------------")
    while(itr is not None):
      print(itr.value)
      itr = itr.next
    print("-----------------------------")
    print()

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.print()

print(dll.pop().value)
print(dll.pop().value)
print(dll.pop())
dll.print()

dll.prepend(2)
dll.prepend(1)
dll.prepend(0)
dll.print()

print(dll.get_node(0).value)
print(dll.get_node(1).value)
dll.get_node(-1)
dll.get_node(5)

dll.set_node(0,1)
dll.set_node(1,2)
dll.set_node(2,3)
dll.set_node(-1,-1)
dll.set_node(5,5)
dll.print()

dll.insert(0,-1)
dll.insert(2,1.5)
dll.insert(4,2.5)
dll.print()

print(dll.remove(0).value)
print(dll.remove(1).value)
print(dll.remove(3).value)
dll.print()

print(dll.pop_first().value)
print(dll.pop_first().value)
print(dll.pop_first().value)
print(dll.pop_first())
dll.print()