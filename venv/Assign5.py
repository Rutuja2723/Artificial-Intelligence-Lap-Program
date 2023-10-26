import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, weight))

    def dijkstra(self, start):
        # Initialize distance dictionary with initial distances to all nodes set to infinity
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        # Priority queue for nodes to visit
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Check if the current distance is outdated
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # If a shorter path is found, update the distance and add to the queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'A', 7)

start_node = 'A'
shortest_distances = graph.dijkstra(start_node)

for node, distance in shortest_distances.items():
    print(f'Shortest distance from {start_node} to {node} is {distance}')
