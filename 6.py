from FlightGraph import *

if __name__ == "__main__":

    grp = Graph()

    # airportA = Airport("A", 20, 20, False)
    # airportB = Airport("B", 15, 10, False)
    # airportC = Airport("C", 40, 30, True)
    # airportD = Airport("D", 35, 80, True)
    # airportE = Airport("E", 75, 120, False)
    # airportF = Airport("F", 60, 70, True)

    airports = {}
    while True:
        print("Digite 'Sair' para encerrar a inserção.")
        input_str = input(" Insira as informações dos Aeroportos (Nome, Tempo De Parada, Custo, Parada Obrigatória (S / N)): ")

        string_list = [s.strip() for s in input_str.split(',')]

        if "sair" in string_list or "Sair" in string_list:
            break
        
        if len(string_list) < 4:
            print("Informações inválidas")
            continue

        if string_list[3] == 'S' : weigh_in = True
        else: weigh_in = False

        airport = Airport(string_list[0], int(string_list[1]), float(string_list[2]), weigh_in)
        print(str(airport))
        airports[string_list[0]] = airport

    while True:
        print("Digite 'Sair' para encerrar a inserção.")
        input_str = input(" Insira as conexões separadas por virgula, Ex: A, B . Um por linha: ")

        string_list = [s.strip() for s in input_str.split(',')]

        if "sair" in string_list or "Sair" in string_list:
            break   
        
        if string_list[0] not in airports or string_list[1] not in airports:
            print("Aeroporto nao registrado")
            continue

        grp.add_edge(airports.get(string_list[0]), airports.get(string_list[1]))

    while True:
        print("Digite 'Sair' para encerrar a inserção.")
        input_str = input("Defina o voo (De, Para, Tempo Maximo de Espera): ")

        string_list = [s.strip() for s in input_str.split(',')]
        maxTime = int(string_list[2])
        print(grp.djikstra(airports.get(string_list[0]), airports.get(string_list[1]), maxTime))

