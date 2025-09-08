from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        ## Do traversal then count the no. of times we do traversal in components ==> that woukd be the no. of provinces
        a = len(isConnected)
        visited = [0] * (a)
        provinces = 0
        ### loop controlling components
        for i in range(a):
            # for not traversing those which are traversed
            if not visited[i]:
                provinces += 1
                self.bfs(i, isConnected, visited)

        return provinces
                

    ### traversing for all nodes in a matrix
    def bfs(self, node, isConnected: List[List[int]], visited):
        visited[node] = 1
        for neighbour in range(len(isConnected)):
            ## checking for connection/edge and if not explored
            if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                self.bfs(neighbour, isConnected, visited)
        
            




