class Graph:

    def __init__(self, v):
        self.vertices = v
        self.matrix = [[float('inf') for _ in range(v)] for _ in range(v)]

    def add_edge(self, i, j, weight, bidirectional=False):
        self.matrix[i][j] = weight
        if bidirectional: self.matrix[j][i] = weight

    def minKey(self, key, mstSet):

        min = float('inf')

        for x in range(self.vertices):
            if key[x] < min and mstSet[x] == False:
                min = key[x]
                min_index = x
        
        return min_index
    
    def printMST(self, parent):
        total = 0
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(chr(65 + parent[i]), "-", chr(65 + i), "\t", self.matrix[parent[i]][i])
            total+=self.matrix[parent[i]][i]
        return total

    def primMst(self):

        key = [float('inf')] * self.vertices
        parent = [None] * self.vertices

        key[0] = 0
        mstSet = [False] * self.vertices

        parent[0] = -1

        for x in range(self.vertices):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for j in range(self.vertices):
                if self.matrix[u][j] > 0 and mstSet[j] == False \
                and key[j] > self.matrix[u][j]:

                    key[j] = self.matrix[u][j]
                    parent[j] = u
        
        return self.printMST(parent)
    
    def floyd(self):

        resMatrx = self.matrix

        prev = [[None] * self.vertices for _ in range(self.vertices)]
        nodes = [i for i in range(0,self.vertices)]

        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.matrix[i][j] != -1:
                    prev[i][j] = nodes[i]
        

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range (self.vertices):
                      if resMatrx[i][j] > resMatrx[i][k] + resMatrx[k][j]:
                        resMatrx[i][j] = resMatrx[i][k] + resMatrx[k][j]
                        prev[i][j] = prev[k][j]

        
        return prev
    
    def reconstruct_path(self, previous_node, start, end):
        nodes = [i for i in range(len(previous_node))]
        path = []
        current = end
        while current is not None and current != start:
            path.append(chr(65 + current))
            current = previous_node[nodes.index(start)][nodes.index(current)]
        if current is None:
            print(f"No path from {start} to {end}.")
            return
        path.append(chr(65 + start))
        path.reverse()
        return path
            



