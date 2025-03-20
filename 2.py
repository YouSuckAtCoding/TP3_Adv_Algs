from Graph import Graph

if __name__ == "__main__":

    grp = Graph()

    grp.add_edge("Bairro X", "Bairro Y", 8)
    grp.add_edge("Bairro X", "Bairro Z", 5)
    grp.add_edge("Bairro Y", "Bairro Z", 2)
    grp.add_edge("Bairro Y", "Bairro W", 10)
    grp.add_edge("Bairro Z", "Bairro V", 6)
    grp.add_edge("Bairro V", "Bairro W", 3)


    print(grp.djikstra("Bairro X", "Bairro Y"))