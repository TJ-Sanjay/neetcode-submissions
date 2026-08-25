class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r=len(grid)
        c=len(grid[0])

        dire=[(1,0),(0,1),(-1,0),(0,-1)]

        que=deque()
        vis=set()

        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    que.append((i,j))
                    vis.add((i,j))
        
        dis=0

        while que:
            for _ in range(len(que)):
                x,y=que.popleft()
                grid[x][y]=dis
                for i,j in dire:
                    m,n=x+i,y+j
                    if 0<=m<r and 0<=n<c and (m,n) not in vis and grid[m][n]!=-1:
                        vis.add((m,n))
                        que.append((m,n))
            dis+=1
        


