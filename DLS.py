from collections import defaultdict


class Graph:

    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)

    def dls(self,src,dest,path,level,depth):
        path.append(src)
        if src == dest:
            return path
        if level == depth:
            return False
        for child in self.adj_list[src]:
            if self.dls(child,dest,path,level+1,depth):
                return path
            path.pop()
        return False


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


src = int(input("Enter Source Vertex "))
dest = int(input("Enter Destination Vertex "))
depth = int(input("Enter the MAX Depth for DLS : "))

temp = list()
path = g.dls(src,dest,temp,0,depth)
if path:
    print('Path from ', src, ' to ', dest, ' : ',path)
else:
    print('No path found from given source to destination and depth')


