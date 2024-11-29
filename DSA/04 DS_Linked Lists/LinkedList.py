class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value = None):
    if(value == None):
      self.head = None
      self.tail = None
      # self.length = 0
      return
    node = Node(value)
    self.head = node
    self.tail = node
    # self.length = 1

  def append(self, value):
    node = Node(value)

    # Edge Case: 1
    if(self.head is None):
    # if(self.length is 0):
      self.head = node
      self.tail = node
      # self.length = 1
      return True

    self.tail.next = node
    self.tail = node
    # self.length += 1
    return True

  def pop(self):
    # Edge Case: 1
    if(self.head is None):
      return None
    
    # Edge Case: 2
    if(self.head is self.tail):
      ele = self.head
      self.head = None
      self.tail = None
      # self.length -= 1
      return ele

    backItr = self.head
    frontItr = self.head.next
    while(frontItr is not self.tail):
      backItr = frontItr
      frontItr = frontItr.next
    self.tail = backItr
    self.tail.next = None
    # self.length -= 1
    return frontItr

  def prepend(self, value):
    node = Node(value)

    # Edge Case: 1
    if(self.head is None):
      self.head = node
      self.tail = node
      return True
    
    node.next = self.head
    self.head = node
    return True

  def pop_first(self):
    # Edge Case: 1
    if(self.head is None):
      return None
    
    # Edge Case: 2
    if(self.head is self.tail):
      ele = self.head
      self.head = None
      self.tail = None
      return ele
    
    ele = self.head
    self.head = self.head.next
    ele.next = None
    return ele
  
  def get_node(self, index):
    # Edge Case: 1
    if(index < 0):
      print("Negative Index")
      return None
    
    itr = self.head
    incr = 0
    while(itr is not None and incr < index):
      itr = itr.next
      incr += 1

    # Edge Case: 2
    if(itr is None):
      print("Index out of Bound")
      return None

    return itr

  def set_node(self, index, value):
    ele = self.get_node(index)
    if (ele is None):
      return False

    ele.value = value
    return True

  def insert(self, index, value):
    # Edge Case: 1
    if(index == 0):
      return self.prepend(value)

    prev_node = self.get_node(index-1)
    # Edge Case: 2
    if(prev_node is None):
        return False

    node = Node(value)
    node.next = prev_node.next
    prev_node.next = node
    return True
  
  def remove(self, index):
    # Edge Case: 1
    if(index == 0):
      return self.pop_first()
    
    prev_node = self.get_node(index-1)
    # Edge Case: 2
    if (prev_node is None):
      return None

    ele = prev_node.next
    prev_node.next = ele.next
    ele.next = None
    return ele
  
  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp

    backItr = None
    mid = self.tail
    frontItr = self.tail.next
    while(frontItr is not None):
      mid.next = backItr
      backItr = mid
      mid = frontItr
      frontItr = mid.next
    # Edge Case: 1
    mid.next = backItr

  def print(self):
    itr = self.head
    print()
    print("-----------------------------")
    while(itr is not None):
      print(itr.value)
      itr = itr.next
    print("-----------------------------")
    print()
    
ll = LinkedList()
ll.print()

ll.append(1)
ll.append(2)
ll.print()

ll.pop()
ll.pop()
ll.pop()
ll.print()

ll.prepend(0)
ll.prepend(-1)
ll.print()

ll.get_node(-1)
ll.get_node(0)
ll.get_node(1)
ll.get_node(2)
ll.get_node(55)
ll.print()

ll.set_node(-1, -1)
ll.set_node(0, 0)
ll.set_node(1, 1)
ll.set_node(2, 2)
ll.print()

ll.insert(-1, -1)
ll.insert(0, -1)
ll.insert(1,0.5 )
ll.insert(3, 1.5)
ll.insert(6, 3)
ll.print()

ll.reverse()
ll.print()

ll.remove(-1)
ll.remove(0)
ll.remove(1)

ll.pop_first()
ll.pop_first()
ll.pop_first()
ll.print()