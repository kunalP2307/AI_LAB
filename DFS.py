from collections import defaultdict

class Graph:

    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)

    def dfs(self,source):
        stack = []
        visited = []

        for i in range(len(self.adj_list)):
            visited.append(False)

        stack.append(source)

        while stack:
            source = stack[-1]
            stack.pop()

            if visited[source] == False:
                print(source,end=" ")
                visited[source] = True

            for vertex in self.adj_list[source]:
                if visited[vertex] == False:
                    stack.append(vertex)


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
print("Depth First Search for Given Graph Starting from Vertex : ",source)
g.dfs(source)