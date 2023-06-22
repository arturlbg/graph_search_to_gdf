# This project provides the ability to load a Graph from a text file, conduct Graph Searches, assign colors to edges, and generate a GDF file that represents the search results.
+ Graph Loading: It reads a graph from a text file in the TXT format. +

+ Graph Search: It conducts two types of graph searches:
    Depth-First Search (DFS): Traverses the graph using the depth-first search algorithm.
    Breadth-First Search (BFS): Traverses the graph using the breadth-first search algorithm. +

+ Graph Coloring: During the search process, the edges of the graph are assigned different colors based on path choice. Specifically, the colors used can include blue, green, and red. +

+ GDF File Conversion: After performing the search, the project converts the search results into a GDF (Graph Description Format) file. This file represents the graph along with the assigned colors for the edges. +

Run it yourself:
The graph examples are located in the "in" folder. When running the command ```python main.py```, the GDF files are generated inside the "out" folder.

You can visualize the generated graph by importing it into the Gephi program for graphical representation.

+ ![image](https://github.com/arturlbg/graph_search_to_gdf/assets/60628919/7b6ce09a-33b7-44e6-a85a-b9d84e77ab5e)

