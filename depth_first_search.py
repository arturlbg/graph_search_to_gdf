import numpy as np

class depth_first:
  def __init__(self, graph):
    self.adjacency = graph.to_adjacency()
    self.matrix = graph.to_matrix()
    self.n = len(self.adjacency)
    self.t = 0
    self.PE = np.zeros(self.n)
    self.PS = np.zeros(self.n)
    self.fathers = np.zeros(self.n)
    self.edge_colors = []

  def run(self, idx):
    self.t+=1
    self.PE[idx] = self.t
    v = self.adjacency[idx] 
    
    for i in v:
      if self.PE[i-1] == 0:
        self.insert_ordenate(idx+1, i, "BLUE")
        self.fathers[i-1] = idx
        self.run(i-1)
      else:
        if self.PS[idx] == 0 and i != self.fathers[idx]:
          self.insert_ordenate(idx+1, i, "RED")
    self.t+=1
    self.PS[idx] = self.t
    self.edge_colors.sort(key=lambda x: (x[0][0], x[0][1]))

  def insert_ordenate(self, v, w, color):
    if v>w:
      edge = (w,v)
    else:
      edge = (v,w)
    info = [edge, color]
    if edge not in [i[0] for i in self.edge_colors]:
      self.edge_colors.append(info)