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

    grp.add_edge(0,1,20)
    grp.add_edge(0,2,40)
    grp.add_edge(1,2,10)
    grp.add_edge(1,3,30)
    grp.add_edge(2,3,20)
    grp.add_edge(2,4,30)
    grp.add_edge(3,4,10)
    
    print(grp.matrix)

    prev = grp.floyd()
    print(prev)

    print(grp.reconstruct_path(prev, 1,4))
    

