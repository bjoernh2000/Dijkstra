import sys
import heapq

class Node:  # Node class to keep track of distance, index and parent node
    def __init__(self, d, i):
        self.dist = d  #distance
        self.index = i  # index
        self.parent = None  # set to Null
        self.visited = False

    def __lt__(self,other):  # less than function, required for min heap
        return self.dist < other.dist
    
    def __gt__(self,other):  # greater than function, required for min heap
        return self.dist > other.dist

def dijkstra(nodes, source):  # function for running dijkstra from source node
    global vertices
    unvisited = nodes
    sourceNode = nodes[source]
    sourceNode.dist = 0
    visited = []  # min heap to keep track of next min neighbour
    heapq.heappush(visited, sourceNode)  # push source onto heap
    while visited != []:  # while len(explored<vertices)
        curr = heapq.heappop(visited)
        currIndex = curr.index
        currDist = curr.dist
        if not curr.visited:
            curr.visited = True
            if len(adjList[currIndex]) != 0:
                for x in adjList[currIndex]:
                    weight = x[0]
                    index = x[1]
                    newDistance = weight + currDist
                    neighbourNode = unvisited[index]
                    if newDistance < neighbourNode.dist:
                        neighbourNode.parent = curr
                        neighbourNode.dist = newDistance
                        heapq.heappush(visited, neighbourNode)
    for x in unvisited:
        if x.dist != float('inf') and x.dist!=0:
            sys.stdout.write(str(x.index) + " " + str(x.dist) + " " + str(x.parent.index)+"\n")

lines = sys.stdin.readlines()
firstline = lines[0]
[vertices, edges, source] = firstline.split()
vertices = int(vertices)
edges = int(edges)
source = int(source)
otherLines = lines[1:]
adjList = [[] for i in range(vertices)]  #adjacency list


for i in range(len(otherLines)):
    x = otherLines[i]
    [ini, outi, weight] = x.split()
    ini = int(ini)
    outi = int(outi)
    weight = int(weight)
    adjList[ini].append([weight, outi])

nodes = [Node(float('inf'),i) for i in range(vertices)]

dijkstra(nodes,source)
