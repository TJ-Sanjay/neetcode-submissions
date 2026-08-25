class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)==n-1:
            graph={i:[] for i in range(n)}

            for i,j in edges:
                graph[i].append(j)
                graph[j].append(i)


            

            que=deque()
            

            vis=set()
         

            for k in range(n):
                if k in vis:
                    continue
                que.append((k,-1))
                while que:
                    node,parent=que.popleft()
                    vis.add(node)
                    for nei in graph[node]:
                        if nei!=parent:
                            if nei in vis:
                                return False
                            que.append((nei,node))
            return True
        else:
            return False
                    
