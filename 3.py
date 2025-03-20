from Graph import Graph

if __name__ == "__main__":

    grp = Graph()

    grp.add_edge("GRU", "GIG", 360)
    grp.add_edge("GRU", "BSB", 850)
    grp.add_edge("GIG", "BSB", 930)
    grp.add_edge("BSB", "REC", 1650)
    grp.add_edge("GRU", "POA", 870)
    grp.add_edge("POA", "REC", 3000)

    print(grp.djikstra("GRU", "POA"))