from MatrixGraph import Graph

if __name__ == "__main__":

    grp = Graph(5)

    #Matriz sem pesos negativos
    
    # Cidade A - Cidade B - Cidade C - Cidade D - Cidade - E
    # A -> B
    # A -> C
    # B -> D
    # C -> D
    # C -> E  
    # D -> E
    
    grp.add_edge(0,1,40, True)
    grp.add_edge(0,2,150, True)
    grp.add_edge(1,2,170, True)
    grp.add_edge(1,3,65, True)
    grp.add_edge(2,3,82, True)
    grp.add_edge(2,4,39, True)
    grp.add_edge(3,4,18, True)
    
    print(grp.matrix)

    total = grp.primMst()

    print("Valor do conjunto mais econômico: ", total)


    

