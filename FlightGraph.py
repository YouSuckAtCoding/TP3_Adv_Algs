import heapq
  
class Airport:

    def __init__(self, name, stoptime, cost, weigh_in):
        self.Name = name
        self.StopTime = stoptime
        self.Cost = cost
        self.Weigh_in = weigh_in

    def __str__(self):
        return str(f"{self.Name, self.StopTime, self.Cost, self.Weigh_in}")

class Graph:

    def __init__(self):
        self.list = {}
    
    def add_edge(self, airport1, airport2):
        if airport1 not in self.list:
            self.list[airport1] = []
        self.list[airport1].append((airport2))

        if airport2 not in self.list:
            self.list[airport2] = []
        self.list[airport2].append((airport1))
    
    def djikstra(self, src, dest, maxStopTime):

        cost = {edge: float('inf') for edge in self.list}
        time = {edge: float('inf') for edge in self.list}
        prev = {edge: None for edge in self.list}

        cost[src] = 0
        time[src] = 0
        pq = [(0, src)]

        while pq:

            curr_cost, curr_airport = heapq.heappop(pq)

            if curr_airport == dest:
                return self.getShortestPath(src, dest, prev)
            
            for airport in self.list[curr_airport]:
                
                newTime = curr_airport.StopTime + airport.StopTime
                
                if newTime < time[airport]:
                    maxStopTime -= newTime
                    if maxStopTime <= 0:
                        continue

                newCost = curr_cost + (airport.Cost + airport.Weigh_in)
               
                if newCost < cost[airport]:
                    cost[airport] = newCost
                    time[airport] = newTime
                    prev[airport] = curr_airport
                    heapq.heappush(pq, (newCost, airport))
        
        return []

    def getShortestPath(self, src, dest, prev):
        path = []
        current_edge = dest

        while current_edge is not None:
            path.append(current_edge.Name)
            current_edge = prev[current_edge]
        path.reverse()
        return path if path[0] == src.Name else []




        
