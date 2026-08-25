class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
         graph={i:[] for i in range(n)}

         for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

         que=deque()
        
         vis=set()
         res=0

         for k in range(n):
             if k in vis:
                 continue
             que.append((k,-1))
             while que:
                 node,parent=que.popleft()
                 vis.add(node)
                 for nei in graph[node]:
                     if nei!=parent and nei not in vis:
                         que.append((nei,node))
             res+=1
         return res
        



