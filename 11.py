from MatrixGraph import Graph

if __name__ == "__main__":

    grp = Graph(5)

    #Matriz sem pesos negativos
    
    # Operadora A - Operadora B - Operadora C - Operadora D - Operadora - E
    # A -> B
    # A -> C
    # B -> D
    # C -> D
    # C -> E  
    # D -> E
    
    grp.add_edge(0,1,75, True)
    grp.add_edge(0,2,95, True)
    grp.add_edge(1,2,62, True)
    grp.add_edge(1,3,45, True)
    grp.add_edge(2,3,140, True)
    grp.add_edge(2,4,30, True)
    grp.add_edge(3,4,60, True)
    
    print(grp.matrix)

    grp.primMst()
    

