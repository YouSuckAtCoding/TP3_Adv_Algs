from SmartCityGraph import *

if __name__ == "__main__":

    grp = Graph()

    streetA = Street("A", 20, 30, 1, False)
    streetB = Street("B", 15, 10, 2, True)
    streetC = Street("C", 40, 25, 1, False)
    streetD = Street("D", 35, 28, 3, True)
    streetE = Street("E", 75, 45, 2, False)
    streetF = Street("F", 60, 40, 1, True)
    vehicle = Vehicle(150)


    grp.add_edge(streetA, streetB)
    grp.add_edge(streetA, streetD)
    grp.add_edge(streetB, streetC)
    grp.add_edge(streetC, streetD)
    grp.add_edge(streetB, streetD)
    grp.add_edge(streetC, streetE)
    grp.add_edge(streetC, streetF)

    print(grp.djikstra(streetA, streetD, vehicle))
    print(grp.djikstra(streetA, streetE, vehicle))
    print(grp.djikstra(streetA, streetF, vehicle))
    print(grp.djikstra(streetB, streetF, vehicle))  
    print(grp.djikstra(streetD, streetE, vehicle))
