from Graph import Graph

if __name__ == "__main__":

    grp = Graph()

    grp.add_edge("Cidade A", "Cidade B", 150)
    grp.add_edge("Cidade A", "Cidade C", 200)
    grp.add_edge("Cidade B", "Cidade D", 100)
    grp.add_edge("Cidade C", "Cidade D", 50)
    grp.add_edge("Cidade D", "Cidade E", 120)
    grp.add_edge("Cidade B", "Cidade E", 300)


    print(grp.djikstra("Cidade C", "Cidade E"))