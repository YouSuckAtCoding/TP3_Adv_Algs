from MatrixGraph import Graph

if __name__ == "__main__":

    grp = Graph(5)

    #Matriz sem pesos negativos
    
    # A - B - C - D - E
    # A -> B
    # A -> C
    # B -> D
    # C -> D
    # C -> E  
    # D -> E
    grp.add_edge(0,1,2)
    grp.add_edge(0,2,4)
    grp.add_edge(1,2,1)
    grp.add_edge(1,3,3)
    grp.add_edge(2,3,2)
    grp.add_edge(2,4,3)
    grp.add_edge(3,4,1)
    
    print(grp.matrix)

    grp.primMst()
    

