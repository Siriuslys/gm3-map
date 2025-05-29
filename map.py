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

#---------------------- 2nd Floor ----------------------#
g.addVertex("Home & Living")
g.addVertex("Malinda Furniture Gallery")
g.addVertex("Vivere")
g.addVertex("Idemu")
g.addVertex("Payless Shoes")
g.addVertex("Padre")
g.addVertex("Iuiga")
g.addVertex("Urban Republic")
g.addVertex("Vans")
g.addVertex("Asics")
g.addVertex("The Athlete's Foot")
g.addVertex("Puma")
g.addVertex("New Era")
g.addVertex("The North Face")
g.addVertex("Hoops")
g.addVertex("Seek")
g.addVertex("KKV Lantai 2")
g.addVertex("Lao Fook")
g.addVertex("Pan & Co")
g.addVertex("Planet Sports Asia")
g.addVertex("Converse")
g.addVertex("Crocs")
g.addVertex("Tucano's")
g.addVertex("Adidas")
g.addVertex("Wee Nam Kee")
g.addVertex("Fila")
g.addVertex("eskalator 21 1") 
g.addVertex("eskalator 21 2") 
g.addVertex("eskalator 21 3") 
g.addVertex("eskalator 23 1") 
g.addVertex("eskalator 23 2") 
g.addVertex("eskalator 23 3")
g.addVertex("lift 2 1")
g.addVertex("lift 2 2")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addVertex("f")
g.addVertex("g")
g.addVertex("h")
g.addVertex("i")
g.addVertex("j")
g.addVertex("k")
g.addVertex("l")
g.addVertex("m")
g.addVertex("n")
g.addVertex("o")
g.addVertex("cc")
g.addVertex("dd")
g.addVertex("ss")
g.addVertex("Toilet Lantai 2")

#---------------------- 3rd Floor ----------------------#
g.addVertex("Jiggle Jungle")
g.addVertex("Reformed Exodus Community")
g.addVertex("Magal Korean BBQ")
g.addVertex("Saga Japanese Restaurant")
g.addVertex("LinCafe")
g.addVertex("BonCafe")
g.addVertex("Natural Farm")
g.addVertex("Shinjuku")
g.addVertex("Mi Store")
g.addVertex("Guardian Plus")
g.addVertex("Vlife Medical")
g.addVertex("Huawei")
g.addVertex("Oppo")
g.addVertex("House of David")
g.addVertex("Scoop Ideas")
g.addVertex("Maison Feerie")
g.addVertex("Pure Clinic")
g.addVertex("Puro Clinic")
g.addVertex("Justice")
g.addVertex("Samsung")
g.addVertex("Willio")
g.addVertex("GingerSnaps")
g.addVertex("Mothercare")
g.addVertex("Watsons GM3")
g.addVertex("Nona Manis")
g.addVertex("Toilet Lantai 3")
g.addVertex("eskalator 32 1") 
g.addVertex("eskalator 32 2") 
g.addVertex("eskalator 32 3") 
g.addVertex("eskalator 34 1") 
g.addVertex("eskalator 34 2") 
g.addVertex("eskalator 34 3")
g.addVertex("lift 3 1")
g.addVertex("lift 3 2")
g.addVertex("p")
g.addVertex("q")
g.addVertex("r")
g.addVertex("s")
g.addVertex("t")
g.addVertex("tt")

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

#---------------------- 2nd Floor ----------------------#
g.addEdge("Home & Living", "h", 18)
g.addEdge("h", "Home & Living", 18)
g.addEdge("Malinda Furniture Gallery", "h", 18)
g.addEdge("h", "Malinda Furniture Gallery", 18)
g.addEdge("Vivere", "h", 18)
g.addEdge("h", "Vivere", 18)
g.addEdge("Idemu", "h", 18)
g.addEdge("h", "Idemu", 18)
g.addEdge("Home & Living", "c", 15)
g.addEdge("c", "Home & Living", 15)
g.addEdge("Malinda Furniture Gallery", "c", 15)
g.addEdge("c", "Malinda Furniture Gallery", 15)
g.addEdge("Vivere", "c", 15)
g.addEdge("c", "Vivere", 15)
g.addEdge("Idemu", "c", 15)
g.addEdge("c", "Idemu", 15)
g.addEdge("c", "l", 7)
g.addEdge("l", "c", 7)
g.addEdge("l", "lift 2 1", 8)
g.addEdge("lift 2 1", "l", 8)
g.addEdge("d", "lift 2 1", 8)
g.addEdge("lift 2 1", "d", 8)
g.addEdge("d", "l", 15)
g.addEdge("l", "d", 15)
g.addEdge("Home & Living", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "Home & Living", 21)
g.addEdge("Malinda Furniture Gallery", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "Malinda Furniture Gallery", 21)
g.addEdge("Vivere", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "Vivere", 21)
g.addEdge("Idemu", "eskalator 21 1", 21)
g.addEdge("eskalator 21 1", "Idemu", 21)
g.addEdge("eskalator 21 1", "i", 13)
g.addEdge("i", "eskalator 21 1", 13)
g.addEdge("eskalator 21 1", "cc", 1)
g.addEdge("cc", "eskalator 21 1", 1)
g.addEdge("cc", "dd", 14)
g.addEdge("dd", "cc", 14)
g.addEdge("eskalator 23 1", "cc", 1)
g.addEdge("cc", "eskalator 23 1", 1)
g.addEdge("h", "i", 12)
g.addEdge("i", "h", 12)
g.addEdge("i", "j", 8)
g.addEdge("j", "i", 8)
g.addEdge("j", "Payless Shoes", 9)
g.addEdge("Payless Shoes", "j", 9)
g.addEdge("Payless Shoes", "Padre", 12)
g.addEdge("Padre", "Payless Shoes", 12)
g.addEdge("Padre", "k", 11)
g.addEdge("k", "Padre", 11)
g.addEdge("Urban Republic", "k", 13)
g.addEdge("k", "Urban Republic", 13)
g.addEdge("g", "m", 15)
g.addEdge("m", "g", 15)
g.addEdge("m", "eskalator 21 2", 3)
g.addEdge("eskalator 21 2", "m", 3)
g.addEdge("Urban Republic", "eskalator 21 2", 3)
g.addEdge("eskalator 21 2", "Urban Republic", 3)
g.addEdge("eskalator 21 2", "eskalator 23 2", 5)
g.addEdge("eskalator 23 2", "eskalator 21 2", 5)
g.addEdge("eskalator 23 2", "Urban Republic", 5)
g.addEdge("Urban Republic", "eskalator 23 2", 5)
g.addEdge("n", "eskalator 23 2", 5)
g.addEdge("eskalator 23 2", "n", 5)
g.addEdge("Vans", "n", 6)
g.addEdge("n", "Vans", 6)
g.addEdge("Urban Republic", "Vans", 12)
g.addEdge("Vans", "Urban Republic", 12)
g.addEdge("Vans", "The North Face", 6)
g.addEdge("The North Face", "Vans", 6)
g.addEdge("The North Face", "Hoops", 6)
g.addEdge("Hoops", "The North Face", 6)
g.addEdge("Hoops", "Seek", 8)
g.addEdge("Seek", "Hoops", 8)
g.addEdge("Seek", "KKV Lantai 2", 10)
g.addEdge("KKV Lantai 2", "Seek", 10)
g.addEdge("KKV Lantai 2", "Lao Fook", 17)
g.addEdge("Lao Fook", "KKV Lantai 2", 17)
g.addEdge("Planet Sports Asia", "Pan & Co", 17)
g.addEdge("Pan & Co", "Planet Sports Asia", 17)
g.addEdge("Pan & Co", "Lao Fook", 25)
g.addEdge("Lao Fook", "Pan & Co", 25)
g.addEdge("Planet Sports Asia", "Converse", 12)
g.addEdge("Converse", "Planet Sports Asia", 12)
g.addEdge("Planet Sports Asia", "Crocs", 2)
g.addEdge("Crocs", "Planet Sports Asia", 2)
g.addEdge("Crocs", "Tucano's", 8)
g.addEdge("Tucano's", "Crocs", 8)
g.addEdge("Tucano's", "Adidas", 12)
g.addEdge("Adidas", "Tucano's", 12)
g.addEdge("Adidas", "Wee Nam Kee", 18)
g.addEdge("Adidas", "eskalator 23 3", 8)
g.addEdge("eskalator 23 3", "Adidas", 8)
g.addEdge("eskalator 23 3", "eskalator 21 3", 4)
g.addEdge("eskalator 21 3", "eskalator 23 3", 4)
g.addEdge("eskalator 21 3", "Lao Fook", 5)
g.addEdge("Lao Fook", "eskalator 21 3", 5)
g.addEdge("Lao Fook", "o", 4)
g.addEdge("o", "Lao Fook", 4)
g.addEdge("Planet Sports Asia", "o", 3)
g.addEdge("o", "Planet Sports Asia", 3)
g.addEdge("o", "lift 2 2", 10)
g.addEdge("lift 2 2", "o", 10)
g.addEdge("Planet Sports Asia", "lift 2 2", 10)
g.addEdge("lift 2 2", "Planet Sports Asia", 10)
g.addEdge("Pan & Co", "lift 2 2", 10)
g.addEdge("lift 2 2", "Pan & Co", 10)
g.addEdge("Wee Nam Kee", "Adidas", 18)
g.addEdge("Wee Nam Kee", "Fila", 10)
g.addEdge("Fila", "Wee Nam Kee", 10)
g.addEdge("Fila", "New Era", 8)
g.addEdge("New Era", "Fila", 8)
g.addEdge("New Era", "Puma", 4)
g.addEdge("Puma", "New Era", 4)
g.addEdge("Puma", "The Athlete's Foot", 10)
g.addEdge("The Athlete's Foot", "Puma", 10)
g.addEdge("The Athlete's Foot", "Asics", 6)
g.addEdge("Asics", "The Athlete's Foot", 6)
g.addEdge("Asics", "Iuiga", 8)
g.addEdge("Iuiga", "Asics", 8)
g.addEdge("Hoops", "Puma", 13)
g.addEdge("Puma", "Hoops", 13)
g.addEdge("Lao Fook", "Adidas", 14)
g.addEdge("Adidas", "Lao Fook", 14)
g.addEdge("Fila", "ss", 5)
g.addEdge("ss", "Fila", 5)
g.addEdge("ss", "Wee Nam Kee", 6)
g.addEdge("Wee Nam Kee", "ss", 6)
g.addEdge("Toilet Lantai 2", "ss", 10)
g.addEdge("ss", "Toilet Lantai 2", 10)

#---------------------- 3 Floor ----------------------#
g.addEdge("Jiggle Jungle", "Reformed Exodus Community", 12)
g.addEdge("Reformed Exodus Community", "Jiggle Jungle", 12)
g.addEdge("Reformed Exodus Community", "Magal Korean BBQ", 13)
g.addEdge("Magal Korean BBQ", "Reformed Exodus Community", 13)
g.addEdge("Magal Korean BBQ", "Saga Japanese Restaurant", 19)
g.addEdge("Saga Japanese Restaurant", "Magal Korean BBQ", 19)
g.addEdge("Saga Japanese Restaurant", "LinCafe", 10)
g.addEdge("LinCafe", "Saga Japanese Restaurant", 10)
g.addEdge("LinCafe", "BonCafe", 9)
g.addEdge("BonCafe", "LinCafe", 9)
g.addEdge("BonCafe", "Guardian Plus", 11)
g.addEdge("Guardian Plus", "BonCafe", 11)
g.addEdge("t", "BonCafe", 13)
g.addEdge("BonCafe", "t", 13)
g.addEdge("Guardian Plus", "Vlife Medical", 6)
g.addEdge("Vlife Medical", "Guardian Plus", 6)
g.addEdge("Vlife Medical", "Huawei", 6)
g.addEdge("Huawei", "Vlife Medical", 6)
g.addEdge("Huawei", "Oppo", 6)
g.addEdge("Oppo", "Huawei", 6)
g.addEdge("Oppo", "House of David", 6)
g.addEdge("House of David", "Oppo", 6)
g.addEdge("Oppo", "Pure Clinic", 15)
g.addEdge("Pure Clinic", "Oppo", 15)
g.addEdge("Oppo", "Maison Feerie", 17)
g.addEdge("Maison Feerie", "Oppo", 17)
g.addEdge("House of David", "Justice", 6)
g.addEdge("Justice", "House of David", 6)
g.addEdge("Justice", "Samsung", 9)
g.addEdge("Samsung", "Justice", 9)
g.addEdge("Samsung", "Watsons GM3", 12)
g.addEdge("Watsons GM3", "Samsung", 12)
g.addEdge("Nona Manis", "Mothercare", 14)
g.addEdge("Mothercare", "Nona Manis", 14)
g.addEdge("Mothercare", "GingerSnaps", 13)
g.addEdge("GingerSnaps", "Mothercare", 13)
g.addEdge("GingerSnaps", "Willio", 8)
g.addEdge("Willio", "GingerSnaps", 8)
g.addEdge("Willio", "Puro Clinic", 8)
g.addEdge("Puro Clinic", "Willio", 8)
g.addEdge("Puro Clinic", "Pure Clinic", 6)
g.addEdge("Pure Clinic", "Puro Clinic", 6)
g.addEdge("Pure Clinic", "Maison Feerie", 8)
g.addEdge("Maison Feerie", "Pure Clinic", 8)
g.addEdge("Maison Feerie", "Scoop Ideas", 6)
g.addEdge("Scoop Ideas", "Maison Feerie", 6)
g.addEdge("Scoop Ideas", "Mi Store", 7)
g.addEdge("Mi Store", "Scoop Ideas", 7)
g.addEdge("Shinjuku", "t", 18)
g.addEdge("t", "Shinjuku", 18)
g.addEdge("t", "Mi Store", 5)
g.addEdge("Mi Store", "t", 5)
g.addEdge("Shinjuku", "Natural Farm", 7)
g.addEdge("Natural Farm", "Shinjuku", 7)
g.addEdge("Natural Farm", "Jiggle Jungle", 28)
g.addEdge("Jiggle Jungle", "Natural Farm", 28)
g.addEdge("Jiggle Jungle", "eskalator 32 1", 15)
g.addEdge("eskalator 32 1", "Jiggle Jungle", 15)
g.addEdge("eskalator 32 1", "lift 3 1", 10)
g.addEdge("lift 3 1", "eskalator 32 1", 10)
g.addEdge("eskalator 34 1", "lift 3 1", 12)
g.addEdge("lift 3 1", "eskalator 34 1", 12)
g.addEdge("lift 3 1", "Natural Farm", 7)
g.addEdge("Natural Farm", "lift 3 1", 7)
g.addEdge("eskalator 32 1", "Reformed Exodus Community", 18)
g.addEdge("Reformed Exodus Community", "eskalator 32 1", 18)
g.addEdge("Magal Korean BBQ", "eskalator 32 1", 13)
g.addEdge("eskalator 32 1", "Magal Korean BBQ", 13)
g.addEdge("eskalator 34 2", "Maison Feerie", 5)
g.addEdge("Maison Feerie", "eskalator 34 2", 5)
g.addEdge("Pure Clinic", "eskalator 34 2", 6)
g.addEdge("eskalator 34 2", "Pure Clinic", 6)
g.addEdge("eskalator 34 2", "eskalator 32 2", 7)
g.addEdge("eskalator 32 2", "eskalator 34 2", 7)
g.addEdge("eskalator 32 2", "Oppo", 6)
g.addEdge("Oppo", "eskalator 32 2", 6)
g.addEdge("Huawei", "eskalator 32 2", 7)
g.addEdge("eskalator 32 2", "Huawei", 7)
g.addEdge("eskalator 32 2", "Pure Clinic", 10)
g.addEdge("Pure Clinic", "eskalator 32 2", 10)
g.addEdge("eskalator 32 3", "Nona Manis", 2)
g.addEdge("Nona Manis", "eskalator 32 3", 2)
g.addEdge("Mothercare", "p", 10)
g.addEdge("p", "Mothercare", 10)
g.addEdge("p", "eskalator 32 3", 2)
g.addEdge("eskalator 32 3", "p", 2)
g.addEdge("Mothercare", "eskalator 34 3", 5)
g.addEdge("eskalator 34 3", "Mothercare", 5)
g.addEdge("eskalator 34 3", "Watsons GM3", 11)
g.addEdge("Watsons GM3", "eskalator 34 3", 11)
g.addEdge("Mi Store", "BonCafe", 15)
g.addEdge("BonCafe", "Mi Store", 15)
g.addEdge("Watsons GM3", "r", 7)
g.addEdge("r", "Watsons GM3", 7)
g.addEdge("r", "q", 9)
g.addEdge("q", "r", 9)
g.addEdge("r", "lift 3 2", 8)
g.addEdge("lift 3 2", "r", 8)
g.addEdge("Nona Manis", "q", 10)
g.addEdge("q", "Nona Manis", 10)
g.addEdge("Pure Clinic", "House of David", 13)
g.addEdge("House of David", "Pure Clinic", 13)
g.addEdge("Watsons GM3", "s", 12)
g.addEdge("s", "Watsons GM3", 12)
g.addEdge("s", "Mothercare", 3)
g.addEdge("Mothercare", "s", 3)
g.addEdge("Willio", "tt", 5)
g.addEdge("tt", "Willio", 5)
g.addEdge("GingerSnaps", "tt", 3)
g.addEdge("tt", "GingerSnaps", 3)
g.addEdge("tt", "Toilet Lantai 3", 10)
g.addEdge("Toilet Lantai 3", "tt", 10)

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
    # 1st Floor
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
    # 2nd Floor
    "Home & Living": { 
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "Malinda Furniture Gallery": {
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "Vivere": {
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "Idemu": {
        "lvl": 2,
        "lat": -7.276860724638212,
        "lon": 112.77973573259476
    },
    "Payless Shoes": {
        "lvl": 2,
        "lat": -7.276836937605751,
        "lon": 112.78018308281861
    },
    "Padre": {
        "lvl": 2,
        "lat": -7.276818690908215,
        "lon": 112.78031268588614
    },
    "Iuiga": {
        "lvl": 2,
        "lat": -7.276640370086881,
        "lon": 112.78034231989534
    },
    "Urban Republic": {
        "lvl": 2,
        "lat": -7.2767204463104065,
        "lon": 112.78054386729116
    },
    "Vans": {
        "lvl": 2,
        "lat": -7.2765962353408895,
        "lon": 112.78057924842744
    },
    "Asics": {
        "lvl": 2,
        "lat": -7.276565461303477,
        "lon": 112.78036161580701
    },
    "The Athlete's Foot": {
        "lvl": 2,
        "lat": -7.2765097652382025,
        "lon": 112.78040749663381
    },
    "Puma": {
        "lvl": 2,
        "lat": -7.276435278266959,
        "lon": 112.78044874291436
    },
    "New Era": {
        "lvl": 2,
        "lat": -7.276379624512131,
        "lon": 112.78045446445572
    },
    "The North Face": {
        "lvl": 2,
        "lat": -7.276542712505048,
        "lon": 112.78056372747807
    },
    "Hoops": {
        "lvl": 2,
        "lat": -7.276451222625141,
        "lon": 112.78056278078157
    },
    "Seek": {
        "lvl": 2,
        "lat": -7.276381285357999,
        "lon": 112.78057391507662
    },
    "KKV Lantai 2": {
        "lvl": 2,
        "lat": -7.276278210494553,
        "lon": 112.78058694378853
    },
    "Lao Fook": {
        "lvl": 2,
        "lat": -7.276106705768356,
        "lon": 112.78061739331844
    },
    "Pan & Co": {
        "lvl": 2,
        "lat": -7.2760648370785646,
        "lon": 112.78084431043465
    },
    "Planet Sports Asia": {
        "lvl": 2,
        "lat": -7.276034169681878,
        "lon": 112.78065314388778
    },
    "Converse": {
        "lvl": 2,
        "lat": -7.2759379965479525,
        "lon": 112.7806246400466
    },
    "Crocs": {
        "lvl": 2,
        "lat": -7.275926061113751,
        "lon": 112.78060466127937
    },
    "Tucano's": {
        "lvl": 2,
        "lat": -7.275921713255016,
        "lon": 112.78052965395449
    },
    "Adidas": {
        "lvl": 2,
        "lat": -7.27601887022368,
        "lon": 112.78049104271071
    },
    "Wee Nam Kee": {
        "lvl": 2,
        "lat": -7.27618942493676,
        "lon": 112.78048245627355
    },
    "Fila": {
        "lvl": 2,
        "lat": -7.2763010561743755,
        "lon": 112.78046753256609
    },
    "eskalator 21 1": {
        "lvl": 2,
        "lat": -7.276768553333966,
        "lon": 112.77993624210023
    },
    "eskalator 21 2": {
        "lvl": 2,
        "lat": -7.276717892957947,
        "lon": 112.78051579498236
    },
    "eskalator 21 3": {
        "lvl": 2,
        "lat": -7.276081333843109,
        "lon": 112.78058241025713
    },
    "eskalator 23 1": {
        "lvl": 2,
        "lat": -7.276750932334124,
        "lon": 112.78010500079404
    },
    "eskalator 23 2": {
        "lvl": 2,
        "lat": -7.276671588805115,
        "lon": 112.78052526834352
    },
    "eskalator 23 3": {
        "lvl": 2,
        "lat": -7.276070320701251,
        "lon": 112.7805357795653
    },
    "lift 2 1": {
        "lvl": 2,
        "lat": -7.2766848535805195,
        "lon": 112.78000285737369
    },
    "lift 2 2": {
        "lvl": 2,
        "lat": -7.276068335734408,
        "lon": 112.78074158628732
    },
    "c": {
        "lvl": 2,
        "lat": -7.2767354940717155,
        "lon": 112.77984858382945
    },
    "d": {
        "lvl": 2,
        "lat": -7.276705726973944,
        "lon": 112.78008643126907
    },
    "e": {
        "lvl": 2,
        "lat": -7.27671234188486,
        "lon": 112.78015867464944
    },
    "f": {
        "lvl": 2,
        "lat": -7.276706829458405,
        "lon": 112.78022758372055
    },
    "g": {
        "lvl": 2,
        "lat": -7.276690034557035,
        "lon": 112.78034071688091
    },
    "h": {
        "lvl": 2,
        "lat": -7.276924370984631,
        "lon": 112.77989501641031
    },
    "i": {
        "lvl": 2,
        "lat": -7.276880316109455,
        "lon": 112.78000922022068
    },
    "j": {
        "lvl": 2,
        "lat": -7.276856190818805,
        "lon": 112.78009698796382
    },
    "k": {
        "lvl": 2,
        "lat": -7.276784977442944,
        "lon": 112.78042857503351
    },
    "l": {
        "lvl": 2,
        "lat": -7.276724607564603,
        "lon": 112.77992220943213
    },
    "m": {
        "lvl": 2,
        "lat": -7.2767392846176335,
        "lon": 112.78049941692763
    },
    "n": {
        "lvl": 2,
        "lat": -7.2766484734403605,
        "lon": 112.78056892597806
    },
    "o": {
        "lvl": 2,
        "lat": -7.276056842374558,
        "lon": 112.78063890103869
    },
    "cc": {
        "lvl": 2,
        "lat": -7.276748074104617,
        "lon": 112.77993411470248
    },
    "dd": {
        "lvl": 2,
        "lat": -7.27673170334748,
        "lon": 112.78010290232993
    },
    "ss": {
        "lvl": 2,
        "lat": -7.276248149973625,
        "lon": 112.78047522613974
    },
    "Toilet Lantai 2": {
        "lvl": 2,
        "lat": -7.276233167348593,
        "lon": 112.78036345462385
    },
    # Lantai 3
    "Jiggle Jungle": {
        "lvl": 3,
        "lat": -7.2768155807522135,
        "lon": 112.77981203274476
    },
    "Reformed Exodus Community": {
        "lvl": 3,
        "lat": -7.276920670469963,
        "lon": 112.77985119964342
    },
    "Magal Korean BBQ": {
        "lvl": 3,
        "lat": -7.276902572657988,
        "lon": 112.77998229847361
    },
    "Saga Japanese Restaurant": {
        "lvl": 3,
        "lat": -7.276819262534914,
        "lon": 112.78019573939446
    },
    "LinCafe": {
        "lvl": 3,
        "lat": -7.2768067062172435,
        "lon": 112.78034097815214
    },
    "BonCafe": {
        "lvl": 3,
        "lat": -7.276774794363888,
        "lon": 112.78045280241543
    },
    "Natural Farm": {
        "lvl": 3,
        "lat": -7.276704393831949,
        "lon": 112.78008507861017
    },
    "Shinjuku": {
        "lvl": 3,
        "lat": -7.276710750756692,
        "lon": 112.78015911783064
    },
    "Mi Store": {
        "lvl": 3,
        "lat": -7.276632102832224,
        "lon": 112.7803355059113
    },
    "Guardian Plus": {
        "lvl": 3,
        "lat": -7.276709325876453,
        "lon": 112.78053466667228
    },
    "Vlife Medical": {
        "lvl": 3,
        "lat": -7.276650272627975,
        "lon": 112.78056177976526
    },
    "Huawei": {
        "lvl": 3,
        "lat": -7.276585590749917,
        "lon": 112.7805706154532
    },
    "Oppo": {
        "lvl": 3,
        "lat": -7.276517770284954,
        "lon": 112.78058249674416
    },
    "House of David": {
        "lvl": 3,
        "lat": -7.276450787084471,
        "lon": 112.7805918863121
    },
    "Scoop Ideas": {
        "lvl": 3,
        "lat": -7.276557363961814,
        "lon": 112.78035773868555
    },
    "Maison Feerie": {
        "lvl": 3,
        "lat": -7.2765074076917955,
        "lon": 112.78039719423464
    },
    "Pure Clinic": {
        "lvl": 3,
        "lat": -7.276441246523206,
        "lon": 112.78044212596126
    },
    "Puro Clinic": {
        "lvl": 3,
        "lat": -7.276379592572368,
        "lon": 112.78044967693313
    },
    "Justice": {
        "lvl": 3,
        "lat": -7.27638543776763,
        "lon": 112.78060039319831
    },
    "Samsung": {
        "lvl": 3,
        "lat": -7.276280054241553,
        "lon": 112.78061587802091
    },
    "Willio": {
        "lvl": 3,
        "lat": -7.2762974805384175,
        "lon": 112.78045960484764
    },
    "GingerSnaps": {
        "lvl": 3,
        "lat": -7.276218280056312,
        "lon": 112.78047118741506
    },
    "Mothercare": {
        "lvl": 3,
        "lat": -7.276072583778202,
        "lon": 112.78049628837323
    },
    "Watsons GM3": {
        "lvl": 3,
        "lat": -7.276158821164358,
        "lon": 112.78063212731763
    },
    "Nona Manis": {
        "lvl": 3,
        "lat": -7.2759244360052975,
        "lon": 112.78052488169988
    },
    "eskalator 32 1": {
        "lvl": 3,
        "lat": -7.276764447523618,
        "lon": 112.7799571083359
    },
    "eskalator 32 2": {
        "lvl": 3,
        "lat": -7.276528777251087,
        "lon": 112.78052305072418
    },
    "eskalator 32 3": {
        "lvl": 3,
        "lat": -7.27593611346289,
        "lon": 112.78053035672269
    },
    "eskalator 34 1": {
        "lvl": 3,
        "lat": -7.276746661091991,
        "lon": 112.78011624461203
    },
    "eskalator 34 2": {
        "lvl": 3,
        "lat": -7.2765032092432875,
        "lon": 112.7804546893666
    },
    "eskalator 34 3": {
        "lvl": 3,
        "lat": -7.276093968300472,
        "lon": 112.7805269946881
    },
    "lift 3 1": {
        "lvl": 3,
        "lat": -7.276683296924531,
        "lon": 112.78000978020265
    },
    "lift 3 2": {
        "lvl": 3,
        "lat": -7.276080470184809,
        "lon": 112.7807317850224
    },
    "p": {
        "lvl": 3,
        "lat": -7.275943539344524,
        "lon": 112.78050295489646
    },
    "q": {
        "lvl": 3,
        "lat": -7.275968394003243,
        "lon": 112.78063783383567
    },
    "r": {
        "lvl": 3,
        "lat": -7.276067713553303,
        "lon": 112.78064511852881
    },
    "s": {
        "lvl": 3,
        "lat": -7.276094932115541,
        "lon": 112.7805122393861
    },
    "t": {
        "lvl": 3,
        "lat": -7.276688034426414,
        "lon": 112.78034095702168
    },
    "tt": {
        "lvl": 3,
        "lat": -7.2762454283089255,
        "lon": 112.78046489950918
    },
    "Toilet Lantai 3": {
        "lvl": 3,
        "lat": -7.276231456084858,
        "lon": 112.7803569094794
    },
}