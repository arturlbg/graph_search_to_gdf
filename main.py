from write_gdf import write_gdf
from graph import graph
import os

path = './in'

for arquivo in os.listdir(path):
    if os.path.isfile(os.path.join(path, arquivo)):
        create_graph = graph(path+"/"+arquivo)

        create_gdf_depth = write_gdf(create_graph, idx_start_vertice=0, search_type=0)
        create_gdf_depth.run(arquivo.split(".txt")[0]+"_dfs")

        create_gdf_breadth = write_gdf(create_graph, idx_start_vertice=0, search_type=1)
        create_gdf_breadth.run(arquivo.split(".txt")[0]+"_bfs")

