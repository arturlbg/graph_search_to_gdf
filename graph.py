import numpy as np

class graph:
  def __init__(self, path):
    self.array = self.read_file(path)
    self.n = 0
    if(self.array[1] != ' '):
      self.n = int(self.array[:2])
    else:
      self.n = int(self.array[1])
    self.matrix = self.to_matrix()
    self.adjacency = self.to_adjacency()

  def read_file(self, path):
    with open(path, 'r') as file:
        content = file.read()
    return content

  def to_matrix(self):
    graph_text = self.array[len(str(self.n)):].split()
    graph_text = [int(i) for i in graph_text]
    arr_2d = np.reshape(graph_text, (self.n, self.n))
    return arr_2d

  def to_adjacency(self):
    arr_2d = self.to_matrix()
    adj_list = []
    aux = []
    for i in range(self.n):
      for j in range(self.n):
        if arr_2d[i][j] == 1:
          aux.append(j+1)
      adj_list.append(aux)
      aux = []
    return adj_list