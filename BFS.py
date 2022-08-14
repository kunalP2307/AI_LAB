from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,source,destination):
        self.graph[source].append(destination)

    def bfs(self,source):
        visited = []
        queue = []
        for i in range(len(self.graph)):
            visited.append(False)

        queue.append(source)
        visited[source] = True

        while queue:
            s = queue.pop(0)
            print(s ,end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()

print("Enter Edges (Vertices are labelled as 0 to n-1) ")
while True:
    print("Enter Source And Destination vertex for Edge : ",end = "")
    source = int(input())
    destination = int(input())
    g.add_edge(source,destination)
    choice = int(input("Do You want to Add Another Edge : [y/n] : [1/0] "))
    if choice == 0:
        break


source = int(input("Enter Source Vertex "))
print("Breadth First Search for Given Graph Starting from Vertex : ",source)
g.bfs(source)