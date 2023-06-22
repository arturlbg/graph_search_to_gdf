from breadth_first_search import breadth_first
from depth_first_search import depth_first
import numpy as np
import os

def get_radius_diameter_average(graph):
  n = graph.n
  max_depth = []
  average_distances = []
  for i in range(n):
    aux = breadth_first(graph)
    aux.run(i)
    max_depth.append(max(aux.depths)) #Adiciona o nível máximo do vertice i para todos vertice
    average_distances.append(np.average(aux.depths[aux.depths > 0]))
  diameter = max(max_depth)
  radius = min(max_depth)
  average_dst = np.average(average_distances)

  return int(radius), int(diameter), average_dst

class write_gdf:
  def __init__(self, graph, idx_start_vertice, search_type):
    self.n = graph.n
    self.search_type = search_type

    radius, diameter, average_dst = get_radius_diameter_average(graph)

    self.depth = depth_first(graph)
    self.depth.run(idx_start_vertice)

    self.breadth = breadth_first(graph)
    self.breadth.run(idx_start_vertice)
    print(f"The radius of the graph is {radius}, diameter is {diameter} and average distance is {average_dst}")

  def run(self, file_name):
    search = self.depth if self.search_type == 0 else self.breadth
    edges = [i[0] for i in search.edge_colors]
    colors = [i[1] for i in search.edge_colors]
    
    folder_path = 'out'
    os.makedirs(folder_path, exist_ok=True)

    all_path_name = os.path.join(folder_path, file_name + '.gdf')
    with open(all_path_name, "w") as arch:
      arch.write("nodedef>name VARCHAR,label VARCHAR\n")
      for i in range(self.n):
        label = str(i+1) + "," + str(i+1)
        arch.write(label)
        arch.write("\n")
      arch.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n")
      for edge, color in zip(edges, colors):
        rgb = self.color_to_rgb(color)
        arch.write(f"{edge[0]},{edge[1]},false,{rgb}")
        arch.write("\n")
        
  def color_to_rgb(self, color):
    if color == "RED":
      return "'255,0,0'"
    if color == "BLUE":
      return "'0,0,255'"
    if color == "YELLOW":
      return "'255,255,0'"
    if color == "GREEN":
      return "'0,255,0'"