from flask import Flask, request, render_template, jsonify
import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Stores the graph
        self.vertices = []  # Stores the vertices

    # Function to add a vertex
    def addVertex(self, vertex):
        self.vertices.append(vertex)

    # Function to add an edge with a weight
    def addEdge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = {}
        self.graph[start][end] = weight

    # Function to remove an edge
    def removeEdge(self, start, end):
        if start in self.graph and end in self.graph[start]:
            del self.graph[start][end]
            print("Edge removed")
        else:
            print("Edge not found")

    # Function to perform Dijkstra's algorithm
    def dijkstra(self, start, finish):
        # Variable to store distances from the start vertex
        distance = {vertex: float('inf') for vertex in self.vertices}
        distance[start] = 0

        # Variable to track visited vertices
        visited = {vertex: False for vertex in self.vertices}

        # Variable to store parent vertices
        came_from = {vertex: None for vertex in self.vertices}
        came_from[start] = start

        # Priority queue
        queue = [(0, start)]

        while queue:
            print(queue)
            current_distance, current_vertex = heapq.heappop(queue)

            print(current_vertex)
            visited[current_vertex] = True

            # If the destination is reached, return distance and path
            if current_vertex == finish:
                path = [current_vertex]
                while current_vertex != start:
                    current_vertex = came_from[current_vertex]
                    path.append(current_vertex)
                return distance, path[::-1]  # Reverse path to get the correct order

            if current_vertex in self.graph:
                for next_vertex, weight in self.graph[current_vertex].items():
                    print(current_vertex, next_vertex)
                    if not visited[next_vertex]:
                        if (current_distance + weight < distance[next_vertex]):
                            distance[next_vertex] = current_distance + weight
                            came_from[next_vertex] = current_vertex
                            heapq.heappush(queue, (distance[next_vertex], next_vertex))

        return distance, None

# Instantiate graph object
g = Graph()

# Add vertex
#---------------------- Ground Floor ----------------------#
g.addVertex("H&M Lantai G")
g.addVertex("Djournal Coffee Bar")
g.addVertex("Starbucks Reserve")
g.addVertex("Marks & Spencer")
g.addVertex("Pandora")
g.addVertex("Frank&Co")
g.addVertex("Tumi")
g.addVertex("Pintu Keluar 10")
g.addVertex("Elemis")
g.addVertex("Miss Mondial")
g.addVertex("Sociolla")
g.addVertex("Ling's Sister Jewellery")
g.addVertex("eskalator G1 1") 
g.addVertex("eskalator G1 2")
g.addVertex("eskalator G1 3")
g.addVertex("Melissa Clube")
g.addVertex("Adelle Jewellery")
g.addVertex("Timberland")
g.addVertex("Hyundai")
g.addVertex("Elevatione")
g.addVertex("Max Fashion")
g.addVertex("The Gourmet")
g.addVertex("Pintu Keluar 9")
g.addVertex("lift G 1") 
g.addVertex("lift G 2") 
g.addVertex("Marquine")
g.addVertex("Axel Vinesse")
g.addVertex("Kopi Kenangan")
g.addVertex("Pintu Keluar X") 
g.addVertex("Venchi")
g.addVertex("Loccitane") 
g.addVertex("Toilet Lantai G")
g.addVertex("x")
g.addVertex("qq")

#---------------------- 1st Floor ----------------------#
g.addVertex("eskalator 1G 1") 
g.addVertex("eskalator 1G 2") 
g.addVertex("eskalator 1G 3") 
g.addVertex("eskalator 12 1") 
g.addVertex("eskalator 12 2") 
g.addVertex("eskalator 12 3")
g.addVertex("lift 1 1")
g.addVertex("Uniqlo")
g.addVertex("Amarissa")
g.addVertex("Bridges Optical")
g.addVertex("Cheskee")
g.addVertex("Colorbox")
g.addVertex("The Executive")
g.addVertex("KKV Lantai 1")
g.addVertex("Urban & Co")
g.addVertex("Koi The")
g.addVertex("H&M Lantai 1")
g.addVertex("LockNLock")
g.addVertex("Miniso")
g.addVertex("Carla")
g.addVertex("Parkiran")
g.addVertex("Dr. Specs")
g.addVertex("Stop N Go")
g.addVertex("Levi's")
g.addVertex("Watch Club")
g.addVertex("Polo")
g.addVertex("Glam On")
g.addVertex("Fossil")
g.addVertex("Optik Seis Signature")
g.addVertex("Owl Optical")
g.addVertex("Zeiss Vision Center")
g.addVertex("lift 1 2") 
g.addVertex("y")
g.addVertex("a")
g.addVertex("b")
g.addVertex("aa")
g.addVertex("rr")
g.addVertex("Toilet Lantai 1")

# Add Edge
#---------------------- Ground Floor ----------------------#
g.addEdge("H&M Lantai G", "Djournal Coffee Bar", 29)
g.addEdge("Djournal Coffee Bar", "H&M Lantai G", 29)
g.addEdge("H&M Lantai G", "Starbucks Reserve", 29)
g.addEdge("Starbucks Reserve", "H&M Lantai G", 29)
g.addEdge("Djournal Coffee Bar", "Starbucks Reserve", 8)
g.addEdge("Starbucks Reserve", "Djournal Coffee Bar", 8)
g.addEdge("H&M Lantai G", "Marks & Spencer", 12)
g.addEdge("Marks & Spencer", "H&M Lantai G", 12)
g.addEdge("Marks & Spencer", "Pandora", 17)
g.addEdge("Marks & Spencer", "eskalator G1 3", 5)
g.addEdge("eskalator G1 3", "Marks & Spencer", 5)
g.addEdge("H&M Lantai G", "eskalator G1 3", 7)
g.addEdge("eskalator G1 3", "H&M Lantai G", 7)
g.addEdge("Pandora", "Marks & Spencer", 17)
g.addEdge("H&M Lantai G", "Frank&Co", 18)
g.addEdge("Frank&Co", "H&M Lantai G", 18)
g.addEdge("Pandora", "Tumi", 6)
g.addEdge("Tumi", "Pandora", 6)
g.addEdge("Pintu Keluar 10", "Tumi", 23)
g.addEdge("Tumi", "Pintu Keluar 10", 23)
g.addEdge("Elemis", "Miss Mondial", 6)
g.addEdge("Miss Mondial", "Elemis", 6)
g.addEdge("Sociolla", "Ling's Sister Jewellery", 6)
g.addEdge("Ling's Sister Jewellery", "Sociolla", 6)
g.addEdge("Miss Mondial", "Ling's Sister Jewellery", 5)
g.addEdge("Ling's Sister Jewellery", "Miss Mondial", 5)
g.addEdge("eskalator G1 2", "Tumi", 7)
g.addEdge("Tumi", "eskalator G1 2", 7)
g.addEdge("Melissa Clube", "Adelle Jewellery", 14)
g.addEdge("Adelle Jewellery", "Melissa Clube", 14)
g.addEdge("eskalator G1 2", "Elemis", 14)
g.addEdge("Elemis", "eskalator G1 2", 14)
g.addEdge("Melissa Clube", "Timberland", 7)
g.addEdge("Timberland", "Melissa Clube", 7)
g.addEdge("Timberland", "x", 7)
g.addEdge("x", "Timberland", 7)
g.addEdge("Timberland", "Hyundai", 13)
g.addEdge("Hyundai", "Timberland", 13)
g.addEdge("Hyundai", "Elevatione", 7)
g.addEdge("Elevatione", "Hyundai", 7)
g.addEdge("Max Fashion", "The Gourmet", 4)
g.addEdge("The Gourmet", "Max Fashion", 4)
g.addEdge("The Gourmet", "Pintu Keluar 9", 19)
g.addEdge("Pintu Keluar 9", "The Gourmet", 19)
g.addEdge("eskalator G1 1", "Timberland", 10)
g.addEdge("Timberland", "eskalator G1 1", 10)
g.addEdge("lift G 1", "Timberland", 17)
g.addEdge("Timberland", "lift G 1", 17)
g.addEdge("Max Fashion", "lift G 1", 15)
g.addEdge("lift G 1", "Max Fashion", 15)
g.addEdge("lift G 2", "H&M Lantai G", 10)
g.addEdge("H&M Lantai G", "lift G 2", 10)
g.addEdge("Max Fashion", "eskalator G1 1", 25)
g.addEdge("eskalator G1 1", "Max Fashion", 25)
g.addEdge("Pandora", "Frank&Co", 10)
g.addEdge("Frank&Co", "Pandora", 10)
g.addEdge("Elemis", "Frank&Co", 19)
g.addEdge("Frank&Co", "Elemis", 19)
g.addEdge("Marquine", "Tumi", 7)
g.addEdge("Tumi", "Marquine", 7)
g.addEdge("Marquine", "eskalator G1 2", 4)
g.addEdge("eskalator G1 2", "Marquine", 4)
g.addEdge("Marquine", "Axel Vinesse", 6)
g.addEdge("Axel Vinesse", "Marquine", 6)
g.addEdge("Axel Vinesse", "Adelle Jewellery", 7)
g.addEdge("Adelle Jewellery", "Axel Vinesse", 7)
g.addEdge("Adelle Jewellery", "Sociolla", 15)
g.addEdge("Sociolla", "Adelle Jewellery", 15)
g.addEdge("Hyundai", "Max Fashion", 27)
g.addEdge("Max Fashion", "Hyundai", 27)
g.addEdge("Hyundai", "The Gourmet", 27)
g.addEdge("The Gourmet", "Hyundai", 27)
g.addEdge("Max Fashion", "Pintu Keluar X", 14)
g.addEdge("Pintu Keluar X", "Max Fashion", 14)
g.addEdge("The Gourmet", "Pintu Keluar X", 21)
g.addEdge("Pintu Keluar X", "The Gourmet", 21)
g.addEdge("Hyundai", "Kopi Kenangan", 16)
g.addEdge("Kopi Kenangan", "Hyundai", 16)
g.addEdge("Venchi", "Elemis", 9)
g.addEdge("Elemis", "Venchi", 9)
g.addEdge("Venchi", "Frank&Co", 18)
g.addEdge("Frank&Co", "Venchi", 18)
g.addEdge("Loccitane", "Sociolla", 8)
g.addEdge("Sociolla", "Loccitane", 8)
g.addEdge("Elevatione", "Loccitane", 9)
g.addEdge("Loccitane", "Elevatione", 9)
g.addEdge("qq", "Marks & Spencer", 23)
g.addEdge("Marks & Spencer", "qq", 23)
g.addEdge("Pandora", "qq", 3)
g.addEdge("qq", "Pandora", 3)
g.addEdge("qq", "Toilet Lantai G", 10)
g.addEdge("Toilet Lantai G", "qq", 10)
g.addEdge("H&M Lantai G", "qq", 25)
g.addEdge("qq", "H&M Lantai G", 25)
g.addEdge("qq", "Frank&Co", 10)
g.addEdge("Frank&Co", "qq", 10)
g.addEdge("Hyundai", "eskalator G1 1", 8)
g.addEdge("eskalator G1 1", "Hyundai", 8)
g.addEdge("Venchi", "Tumi", 15)
g.addEdge("Tumi", "Venchi", 15)
g.addEdge("Venchi", "Marquine", 15)
g.addEdge("Marquine", "Venchi", 15)
g.addEdge("Elemis", "Marquine", 17)
g.addEdge("Marquine", "Elemis", 17)
g.addEdge("Max Fashion", "x", 22)
g.addEdge("x", "Max Fashion", 22)
g.addEdge("lift G 1", "x", 7)
g.addEdge("x", "lift G 1", 7)
g.addEdge("x", "Hyundai", 11)
g.addEdge("Hyundai", "x", 11)

#---------------------- 1st Floor ----------------------#
g.addEdge("eskalator 1G 1", "lift 1 1", 8)
g.addEdge("lift 1 1", "eskalator 1G 1", 8)
g.addEdge("Stop N Go", "lift 1 1", 7)
g.addEdge("lift 1 1", "Stop N Go", 7)
g.addEdge("Uniqlo", "lift 1 1", 18)
g.addEdge("lift 1 1", "Uniqlo", 18)
g.addEdge("Uniqlo", "Amarissa", 29)
g.addEdge("Amarissa", "Uniqlo", 29)
g.addEdge("Uniqlo", "eskalator 1G 1", 12)
g.addEdge("eskalator 1G 1", "Uniqlo", 12)
g.addEdge("a", "Stop N Go", 11)
g.addEdge("Stop N Go", "a", 11)
g.addEdge("a", "Uniqlo", 13)
g.addEdge("Uniqlo", "a", 13)
g.addEdge("eskalator 12 1", "Stop N Go", 6)
g.addEdge("Stop N Go", "eskalator 12 1", 6)
g.addEdge("a", "eskalator 1G 1", 1)
g.addEdge("eskalator 1G 1", "a", 1)
g.addEdge("b", "a", 14)
g.addEdge("a", "b", 14)
g.addEdge("b", "eskalator 12 1", 1)
g.addEdge("eskalator 12 1", "b", 1)
g.addEdge("eskalator 1G 1", "aa", 8)
g.addEdge("aa", "eskalator 1G 1", 8)
g.addEdge("aa", "Amarissa", 14)
g.addEdge("Amarissa", "aa", 14)
g.addEdge("Amarissa", "Bridges Optical", 17)
g.addEdge("Bridges Optical", "Amarissa", 17)
g.addEdge("Cheskee", "Bridges Optical", 5)
g.addEdge("Bridges Optical", "Cheskee", 5)
g.addEdge("Colorbox", "Cheskee", 5)
g.addEdge("Cheskee", "Colorbox", 5)
g.addEdge("Colorbox", "The Executive", 15)
g.addEdge("The Executive", "Colorbox", 15)
g.addEdge("KKV Lantai 1", "Urban & Co", 9)
g.addEdge("Urban & Co", "KKV Lantai 1", 9)
g.addEdge("KKV Lantai 1", "Koi The", 4)
g.addEdge("Koi The", "KKV Lantai 1", 4)
g.addEdge("Koi The", "y", 5)
g.addEdge("y", "Koi The", 5)
g.addEdge("y", "H&M Lantai 1", 8)
g.addEdge("H&M Lantai 1", "y", 8)
g.addEdge("LockNLock", "Miniso", 4)
g.addEdge("Miniso", "LockNLock", 4)
g.addEdge("Miniso", "Carla", 10)
g.addEdge("Carla", "Miniso", 10)
g.addEdge("Carla", "H&M Lantai 1", 11)
g.addEdge("H&M Lantai 1", "Carla", 11)
g.addEdge("eskalator 1G 3", "Carla", 4)
g.addEdge("Carla", "eskalator 1G 3", 4)
g.addEdge("Stop N Go", "Dr. Specs", 7)
g.addEdge("Dr. Specs", "Stop N Go", 7)
g.addEdge("eskalator 12 1", "Dr. Specs", 7)
g.addEdge("Dr. Specs", "eskalator 12 1", 7)
g.addEdge("The Executive", "Urban & Co", 8)
g.addEdge("Urban & Co", "The Executive", 8)
g.addEdge("Levi's", "Watch Club", 6)
g.addEdge("Watch Club", "Levi's", 6)
g.addEdge("Watch Club", "Polo", 15)
g.addEdge("Polo", "Watch Club", 15)
g.addEdge("Polo", "Glam On", 6)
g.addEdge("Glam On", "Polo", 6)
g.addEdge("Glam On", "LockNLock", 6)
g.addEdge("LockNLock", "Glam On", 6)
g.addEdge("eskalator 1G 3", "Miniso", 9)
g.addEdge("Miniso", "eskalator 1G 3", 9)
g.addEdge("eskalator 12 3", "eskalator 1G 3", 6)
g.addEdge("eskalator 1G 3", "eskalator 12 3", 6)
g.addEdge("H&M Lantai 1", "eskalator 12 3", 3)
g.addEdge("eskalator 12 3", "H&M Lantai 1", 3)
g.addEdge("Fossil", "Levi's", 5)
g.addEdge("Levi's", "Fossil", 5)
g.addEdge("Fossil", "Optik Seis Signature", 5)
g.addEdge("Optik Seis Signature", "Fossil", 5)
g.addEdge("Optik Seis Signature", "Owl Optical", 8)
g.addEdge("Owl Optical", "Optik Seis Signature", 8)
g.addEdge("eskalator 1G 2", "Optik Seis Signature", 4)
g.addEdge("Optik Seis Signature", "eskalator 1G 2", 4)
g.addEdge("Owl Optical", "Zeiss Vision Center", 6)
g.addEdge("Zeiss Vision Center", "Owl Optical", 6)
g.addEdge("eskalator 1G 2", "Owl Optical", 6)
g.addEdge("Owl Optical", "eskalator 1G 2", 6)
g.addEdge("eskalator 12 2", "Owl Optical", 3)
g.addEdge("Owl Optical", "eskalator 12 2", 3)
g.addEdge("eskalator 1G 2", "eskalator 12 2", 5)
g.addEdge("eskalator 12 2", "eskalator 1G 2", 5)
g.addEdge("Dr. Specs", "Zeiss Vision Center", 5)
g.addEdge("Zeiss Vision Center", "Dr. Specs", 5)
g.addEdge("y", "lift 1 2", 10)
g.addEdge("lift 1 2", "y", 10)
g.addEdge("Watch Club", "rr", 12)
g.addEdge("rr", "Watch Club", 12)
g.addEdge("Polo", "rr", 3)
g.addEdge("rr", "Polo", 3)
g.addEdge("Toilet Lantai 1", "rr", 10)
g.addEdge("rr", "Toilet Lantai 1", 10)

# Add location details (floor, latitude, longitude)
places = {
    # Ground Floor
    "H&M Lantai G": {
        "lvl": 0,
        "lat": -7.27611653269939,
        "lon": 112.7805770422953
    },
    "Djournal Coffee Bar": { 
        "lvl": 0,
        "lat": -7.2757956141528695,
        "lon": 112.78075311626509
    },
    "Starbucks Reserve": { 
        "lvl": 0,
        "lat": -7.275835899256407,
        "lon": 112.78080591201103
    },
    "Marks & Spencer": { 
        "lvl": 0,
        "lat": -7.276106138078035,
        "lon": 112.7804930116227
    },
    "Pandora": { 
        "lvl": 0,
        "lat": -7.276370083709992,
        "lon": 112.78046562730117
    },
    "Frank&Co": { 
        "lvl": 0,
        "lat": -7.276383488317819,
        "lon": 112.78054866202376
    },
    "Tumi": { 
        "lvl": 0,
        "lat": -7.276425146770151,
        "lon": 112.78046238347974
    },
    "Pintu Keluar 10": { 
        "lvl": 0,
        "lat": -7.276483312236508,
        "lon": 112.7807051567325
    },
    "Elemis": { 
        "lvl": 0,
        "lat": -7.276591916555589,
        "lon": 112.78057279021732
    },
    "Miss Mondial": { 
        "lvl": 0,
        "lat": -7.276643002486139,
        "lon": 112.78056654417276
    },
    "Sociolla": {
        "lvl": 0,
        "lat": -7.276772608642432,
        "lon": 112.78045604842669
    },
    "Ling's Sister Jewellery": { 
        "lvl": 0,
        "lat": -7.276702077590642,
        "lon": 112.7805381854883
    },
    "Melissa Clube": { 
        "lvl": 0,
        "lat": -7.276728635983375,
        "lon": 112.78023240394253
    },
    "Adelle Jewellery": { 
        "lvl": 0,
        "lat": -7.2767093976786015,
        "lon": 112.78031664144987
    },
    "Timberland": {
        "lvl": 0,
        "lat": -7.2767412558671225,
        "lon": 112.78017024276835
    },
    "Hyundai": { 
        "lvl": 0,
        "lat": -7.276839263099518,
        "lon": 112.78009735161282
    },
    "Elevatione": { 
        "lvl": 0,
        "lat": -7.276813954903375,
        "lon": 112.78026235408043
    },
    "Max Fashion": { 
        "lvl": 0,
        "lat": -7.276810819372429,
        "lon": 112.77987295695544
    },
    "The Gourmet": { 
        "lvl": 0,
        "lat": -7.276988806491687,
        "lon": 112.77989553323062
    },
    "Pintu Keluar 9": { 
        "lvl": 0,
        "lat": -7.277096814789843,
        "lon": 112.7799339154763
    },
    "lift G 1": {
        "lvl": 0,
        "lat": -7.276694348726551,
        "lon": 112.78000031309045
    },
    "lift G 2": {
        "lvl": 0,
        "lat": -7.276068503898244,
        "lon": 112.78072156282406
    },
    "x": {
        "lvl": 0,
        "lat": -7.276738194892914,
        "lon": 112.7800860111762
    },
    "Marquine": {
        "lvl": 0,
        "lat": -7.276498040083538,
        "lon": 112.78043156105235
    },
    "Axel Vinesse": { 
        "lvl": 0,
        "lat": -7.276588926582775,
        "lon": 112.78037040799222
    },
    "Kopi Kenangan": { 
        "lvl": 0,
        "lat": -7.276951423634216,
        "lon": 112.77996441591858
    },
    "Pintu Keluar X": { 
        "lvl": 0,
        "lat": -7.2766511406737635,
        "lon": 112.77988547319165
    },
    "Venchi": { 
        "lvl": 0,
        "lat": -7.276545594141922,
        "lon": 112.78057442361171
    },
    "Loccitane": { 
        "lvl": 0,
        "lat": -7.2767932820116386,
        "lon": 112.78036900966748
    },
    "Toilet Lantai G": { 
        "lvl": 0,
        "lat": -7.276325297410395,
        "lon": 112.7803358300697
    },
    "eskalator G1 2": {
        "lvl": 0,
        "lat": -7.276515355642729,
        "lon": 112.78046920020836
    },
    "eskalator G1 1": {
        "lvl": 0,
        "lat": -7.276751434411366,
        "lon": 112.78006785734948
    },
    "eskalator G1 3": {
        "lvl": 0,
        "lat": -7.276035075100978,
        "lon": 112.78052649408858
    },
    "qq": {
        "lvl": 0,
        "lat": -7.276337294962175,
        "lon": 112.78046557594735
    },
    # Lantai 1
    "lift 1 1": { 
        "lvl": 1,
        "lat": -7.276685322893826,
        "lon": 112.77998835796643
    },
    "lift 1 2": {
        "lvl": 1,
        "lat": -7.276067130444247,
        "lon": 112.78075380185732
    },
    "y": {
        "lvl": 1,
        "lat": -7.276034574423221,
        "lon": 112.78064743897329
    },
    "Uniqlo": { 
        "lvl": 1,
        "lat": -7.276841158338485,
        "lon": 112.77986302821762
    },
    "Amarissa": {
        "lvl": 1,
        "lat": -7.276846146822336,
        "lon": 112.78009455237975
    },
    "Bridges Optical": { 
        "lvl": 1,
        "lat": -7.276799409539052,
        "lon": 112.78032508801687
    },
    "Cheskee": { 
        "lvl": 1,
        "lat": -7.27679106359534,
        "lon": 112.78038061849804
    },
    "Colorbox": { 
        "lvl": 1,
        "lat": -7.276762926183579,
        "lon": 112.7804621981461
    },
    "The Executive": { 
        "lvl": 1,
        "lat": -7.27660579511398,
        "lon": 112.78058161415652
    },
    "KKV Lantai 1": { 
        "lvl": 1,
        "lat": -7.276296664316362,
        "lon": 112.7805859614005
    },
    "Urban & Co": { 
        "lvl": 1,
        "lat": -7.276518604056193,
        "lon": 112.78055963941671
    },
    "Koi The": { 
        "lvl": 1,
        "lat": -7.27607649716299,
        "lon": 112.78061891360471
    },
    "H&M Lantai 1": { 
        "lvl": 1,
        "lat": -7.275951510046681,
        "lon": 112.78064411395263
    },
    "LockNLock": { 
        "lvl": 1,
        "lat": -7.276079621840211,
        "lon": 112.78049921195407
    },
    "Miniso": { 
        "lvl": 1,
        "lat": -7.275995255540906,
        "lon": 112.78049291186562
    },
    "Carla": { 
        "lvl": 1,
        "lat": -7.275917138583381,
        "lon": 112.78054961264974
    },
    "Parkiran": {
        "lvl": 1,
        "lat": -7.275720605807564,
        "lon": 112.78057834038714
    },
    "Dr. Specs": { 
        "lvl": 1,
        "lat": -7.276713875996165,
        "lon": 112.78015313354086
    },
    "Stop N Go": { 
        "lvl": 1,
        "lat": -7.276716977931656,
        "lon": 112.78006212326454
    },
    "Levi's": { 
        "lvl": 1,
        "lat": -7.276422201208618,
        "lon": 112.78045167404906
    },
    "Watch Club": { 
        "lvl": 1,
        "lat": -7.276361270040056,
        "lon": 112.78045797413552
    },
    "Polo": { 
        "lvl": 1,
        "lat": -7.276211285591501,
        "lon": 112.78048002444109
    },
    "Glam On": { 
        "lvl": 1,
        "lat": -7.276146802400476,
        "lon": 112.78048818680031
    },
    "Fossil": { 
        "lvl": 1,
        "lat": -7.276500592181279,
        "lon": 112.78040251334335
    },
    "Optik Seis Signature": { 
        "lvl": 1,
        "lat": -7.276570561245791,
        "lon": 112.78035928044892
    },
    "Owl Optical": { 
        "lvl": 1,
        "lat": -7.27668905790415,
        "lon": 112.78030580843375
    },
    "Zeiss Vision Center": { 
        "lvl": 1,
        "lat": -7.276701912521091,
        "lon": 112.78022973036184
    },
    "lift 12": { 
        "lvl": 1,
        "lat": -7.27606243611379,
        "lon": 112.7807512154323
    },
    "eskalator 1G 2": {
        "lvl": 1,
        "lat": -7.276629602880476,
        "lon": 112.78036674841582
    },
    "eskalator 1G 1": {
        "lvl": 1,
        "lat": -7.27676952608293,
        "lon": 112.77995343637633
    },
    "eskalator 1G 3": {
        "lvl": 1,
        "lat": -7.275922284219092,
        "lon": 112.78054357264517
    },
    "eskalator 12 1": {
        "lvl": 1,
        "lat": -7.276749303483015,
        "lon": 112.7800890392362
    },
    "eskalator 12 2": {
        "lvl": 1,
        "lat": -7.276683838969902,
        "lon": 112.78037130659726
    },
    "eskalator 12 3": {
        "lvl": 1,
        "lat": -7.275932819942739,
        "lon": 112.78061942343106
    },
    "a": {
        "lvl": 1,
        "lat": -7.276743431982581,
        "lon": 112.77995228926716
    },
    "b": {
        "lvl": 1,
        "lat": -7.276730899799716,
        "lon": 112.78008115541769
    },
    "aa": {
        "lvl": 1,
        "lat": -7.27683835376088,
        "lon": 112.77993627772213
    },
    "rr": {
        "lvl": 1,
        "lat": -7.2762375760276825,
        "lon": 112.78046946234048
    },
    "Toilet Lantai 1": {
        "lvl": 1,
        "lat": -7.276222000225985,
        "lon": 112.78034880293899
    },
}