class Graph:
  def __init__(self):
    self.adj_list = {}

  def add_vertex(self, vertex):
    if vertex in self.adj_list:
      return False
    
    self.adj_list[vertex] = []
    return True
  
  def add_edge(self, vertex1, vertex2):
    # nodes check
    if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
      return False
    
    # adding dup check increase time complexity from O(1) to O(n)
    self.adj_list[vertex2].append(vertex1)
    self.adj_list[vertex1].append(vertex2)
    return True 
  
  def remove_edge(self, vertex1, vertex2):
    # nodes check
    if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
        return False

    # handling removal of non existent edge
    try:
      self.adj_list[vertex1].remove(vertex2)
      self.adj_list[vertex2].remove(vertex1)
    except ValueError:
      pass 
    return True
  
  def remove_vertex(self, vertex):
    if vertex not in self.adj_list:
      return False
    
    for other_vertex in self.adj_list[vertex]:
      self.adj_list[other_vertex].remove(vertex)

    del self.adj_list[vertex]
    return True

  def print(self):
    print()
    print("-----------------------------")
    for k in self.adj_list:
      print(k, " : ", self.adj_list[k])
    print("-----------------------------")
    print()

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('A')
g.print()

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')
g.print()

g.remove_edge('A', 'C')
g.remove_edge('A', 'D')
g.print()

g.remove_vertex('B')
g.remove_vertex('E')
g.print()
