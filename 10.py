from MatrixGraph import Graph

if __name__ == "__main__":

    grp = Graph(5)

    #Matriz sem pesos negativos
    
    # Bairro A - Bairro B - Bairro C - Bairro D - Bairro - E
    # A -> B
    # A -> C
    # B -> D
    # C -> D
    # C -> E  
    # D -> E
    
    grp.add_edge(0,1,212, True)
    grp.add_edge(0,2,420, True)
    grp.add_edge(1,2,301, True)
    grp.add_edge(1,3,320, True)
    grp.add_edge(2,3,120, True)
    grp.add_edge(2,4,241, True)
    grp.add_edge(3,4,97, True)
    
    print(grp.matrix)

    grp.primMst()
    

