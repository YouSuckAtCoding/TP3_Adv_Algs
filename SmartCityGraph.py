import heapq
from enum import Enum

class Traffic(Enum):

    NoTraffic = 1
    Medium = 2
    High = 3
    Congestion = 4

class Vehicle():
    
    def __init__(self, autonomy):
        self.Autonomy = autonomy
        self.MaxAutonomy = autonomy
        
class Street:

    def __init__(self, name, distance, time, traffic=1, recharge=False):
        self.Name = name
        self.Distance = distance
        self.Time = time
        self.Traffic = Traffic(traffic)
        self.HasRecharge = recharge

class Graph:

    def __init__(self):
        self.list = {}
    
    def add_edge(self, street1, street2):
        if street1 not in self.list:
            self.list[street1] = []
        self.list[street1].append(street2)

        if street2 not in self.list:
            self.list[street2] = []
        self.list[street2].append(street1)
    
    def djikstra(self, src, dest, vehicle):

        dist = {edge: float('inf') for edge in self.list}
        time = {edge: float('inf') for edge in self.list}
        prev = {edge: None for edge in self.list}

        dist[src] = 0
        time[src] = 0
        pq = [(0, src)]

        while pq:

            curr_time, curr_street = heapq.heappop(pq)

            if curr_street == dest:
                return self.getShortestPath(src, dest, prev)
            
            for street in self.list[curr_street]:

                newDist = dist[curr_street]+ street.Distance

                if newDist < dist[street]:
                    vehicle.Autonomy -= newDist
                    if vehicle.Autonomy <= 0:
                        if not street.HasRecharge:
                            continue
                        else:
                            vehicle.Autonomy = vehicle.MaxAutonomy
                   
                newTime = curr_time + (street.Time * self.getTrafficPercentage(street.Traffic))

                if newTime < time[street]:
                    dist[street] = newDist
                    time[street] = newTime
                    prev[street] = curr_street
                    heapq.heappush(pq, (newTime, street))
        
        return []

    def getShortestPath(self, src, dest, prev):
        path = []
        current_edge = dest

        while current_edge is not None:
            path.append(current_edge.Name)
            current_edge = prev[current_edge]
        path.reverse()
        return path if path[0] == src.Name else []


    def getTrafficPercentage(self, traffic):

        if traffic == Traffic.NoTraffic:
            return 1
        elif traffic == Traffic.Medium:
            return 1.2
        elif traffic == Traffic.High:
            return 1.7
        else:
            return 2.0
        




        
