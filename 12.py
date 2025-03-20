from Graph import Graph as DjkGraph
from MatrixGraph import Graph as FlydGraph
import time

if __name__ == "__main__":

    djkgrp = DjkGraph()
    flydgrp = FlydGraph(151)


    # Grafo Esparso 
    for i in range(0, 145, 5):
     djkgrp.add_edge(i, i + 5, 10 + i % 10)

    for i in range(0, 140, 10):
      djkgrp.add_edge(i, i + 10, 15 + i % 15)

    for i in range(0, 135, 15):
     djkgrp.add_edge(i, i + 15, 20 + i % 20)

    djkTime = time.time()
    djkgrp.djikstra(0,135)
    print("Tempo djikstra para grafo 1 (esparso) :", time.time() - djkTime)

    for i in range(0, 145, 5):
     flydgrp.add_edge(i, i + 5, 10 + i % 10)

    for i in range(0, 140, 10):
     flydgrp.add_edge(i, i + 10, 15 + i % 15)

    for i in range(0, 135, 15):
     flydgrp.add_edge(i, i + 15, 20 + i % 20)

    flydtime = time.time()
    flydgrp.reconstruct_path(flydgrp.floyd(), 0, 135)

    print("Tempo floyd para grafo 1 (esparso) :", time.time() - flydtime)


    djkgrp = DjkGraph()
    flydgrp = FlydGraph(151)
    # Grafo Denso 
    for i in range(140): 
        for j in range(1, 11):
            djkgrp.add_edge(i, i + j, (i + j) % 25 + 5)

    
    for i in range(140):  
        for j in range(1, 11):
            flydgrp.add_edge(i, i + j, (i + j) % 25 + 5)

    djkTime = time.time()
    djkgrp.djikstra(0, 135)
    print("Tempo djikstra para grafo 2 (denso) :", time.time() - djkTime)

    flydtime = time.time()
    flydgrp.reconstruct_path(flydgrp.floyd(), 0, 135)

    print("Tempo floyd para grafo 2 (denso) :", time.time() - flydtime)

