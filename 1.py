from Graph import Graph
if __name__ == "__main__":

    grp = Graph()

    grp.add_edge("Centro", "A", 5)
    grp.add_edge("Centro", "B", 10)
    grp.add_edge("A", "C", 3)
    grp.add_edge("B", "C", 1)
    grp.add_edge("C", "D", 2)
    grp.add_edge("B", "D", 7)

    print(grp.djikstra("A", "D"))