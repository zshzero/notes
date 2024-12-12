class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None
    
class Stack:
  def __init__(self, value = None):
    if not value:
      self.top = None
      return
    
    node = Node(value)
    self.top = node

  def push(self, value):
    node = Node(value)

    # Edge Case: 1
    if not self.top:
      self.top = node
      return True

    node.next = self.top
    self.top = node
    return True
  
  def pop(self):
    # Edge Case: 1
    if not self.top:
      return None
    
    ele = self.top 
    self.top = ele.next
    ele.next = None
    return ele

  def print(self):
    itr = self.top
    print()
    print("-----------------------------")
    while itr:
      print(itr.value)
      itr = itr.next
    print("-----------------------------")
    print()

s = Stack()
s.print()

s.push(1)
s.push(2)
s.print()

s.pop()
s.pop()
s.pop()
s.print()

class Queue:
  def __init__(self, value = None):
    if not value:
      self.first, self.last = None, None
      return
    
    node = Node(value)
    self.first = node
    self.last = node

  def enqueue(self, value):
    node = Node(value)
    # Edge Case: 1
    if not self.last:
      self.last, self.first = node, node
      return True
    
    self.last.next = node
    self.last = node
    return True
  
  def dequeue(self):
    # Edge Case: 1
    if not self.first:
      return None
    
    ele = self.first
    # Edge Case: 2
    if self.first is self.last:
      self.first, self.last = None, None
      return ele
    
    self.first = ele.next
    ele.next = None
    return ele

  def print(self):
    itr = self.first
    print()
    print("-----------------------------")
    while itr:
      print(itr.value)
      itr = itr.next
    print("-----------------------------")
    print()

q = Queue()
q.print()

q.enqueue(1)
q.enqueue(2)
q.print()

q.dequeue()
q.dequeue()
q.dequeue()
q.print()