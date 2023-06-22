import numpy as np

class breadth_first:
  def __init__(self, graph):
    self.adjacency = graph.to_adjacency()
    self.n = len(self.adjacency)
    self.edge_colors = [] 
    self.depths = np.zeros(self.n)

  def run(self, idx):
    t = 0
    queue = []
    fathers = [-1] * self.n
    L = np.zeros(self.n)

    L[idx] = 1
    queue.append(idx+1)
    while queue:
      v = queue.pop(0)
      for w in self.adjacency[v-1]:
        if L[w-1] == 0:
          self.insert_ordenate(v, w, "BLUE")
          t += 1
          fathers[w-1] = v
          self.depths[w-1] = self.depths[v-1] + 1
          L[w-1] = t
          queue.append(w)
        else:
          if self.depths[v-1] + 1 == self.depths[w-1]: 
            self.insert_ordenate(v, w, "GREEN")
          elif fathers[v-1] == fathers[w-1] and self.depths[v-1] == self.depths[w-1]:
            self.insert_ordenate(v, w, "RED")
          elif fathers[v-1] != fathers[w-1] and self.depths[v-1] == self.depths[w-1]:
            self.insert_ordenate(v, w, "YELLOW")
    self.edge_colors.sort(key=lambda x: (x[0][0], x[0][1]))

  def insert_ordenate(self, v, w, color):
    if v>w:
      edge = (w,v)
    else:
      edge = (v,w)
    info = [edge, color]
    if edge not in [i[0] for i in self.edge_colors]:
      self.edge_colors.append(info)