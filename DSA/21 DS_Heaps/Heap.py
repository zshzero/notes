class MaxHeap:
  def __init__(self):
    self.heap = []

  def _left_child(self, index):
    return 2 * index + 1
  
  def _right_child(self, index):
    return 2 * index + 2
  
  def _parent(self, index):
    return (index - 1) // 2
  
  def _swap_nodes(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

  def _sink_down(self, index):
    if self._left_child(index) <= 0 and self._right_child(index) <= 0:
      return False

    curr = index
    max_ptr = index
    while True:
      left_child = self._left_child(curr)
      right_child = self._right_child(curr)

      if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_ptr]:
        max_ptr = left_child
      if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_ptr]:
        max_ptr = right_child

      if curr != max_ptr:
        self._swap_nodes(curr, max_ptr)
        curr = max_ptr
      else:
        return   

  def insert(self, value):
    self.heap.append(value)
    
    curr = len(self.heap) - 1
    while curr > 0 and self.heap[curr] > self.heap[self._parent(curr)]:
      self._swap_nodes(curr, self._parent(curr))
      curr = self._parent(curr)

  def remove(self):
    if len(self.heap) == 0:
      return None
    
    if len(self.heap) == 1:
      return self.heap.pop()
    
    max_value = self.heap[0]
    self.heap[0] =  self.heap.pop()
    self._sink_down(0)

    return max_value

  def print(self):
    print()
    print("-----------------------------")
    print(self.heap)
    print("-----------------------------")
    print()

h = MaxHeap()
h.insert(99)
h.insert(72)
h.insert(61)
h.insert(58)
h.print()

h.insert(100)
h.print()

h.insert(75)
h.print()

print(h.remove())
h.print()