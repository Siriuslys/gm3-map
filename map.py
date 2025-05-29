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
