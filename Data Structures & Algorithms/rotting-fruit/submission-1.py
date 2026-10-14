class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalBananas, rottenBananas = 0, 0 
        n, m = len(grid), len(grid[0])
        dq = deque()
        seen = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    pass
                elif grid[i][j] == 1:
                    totalBananas += 1
                elif grid[i][j] == 2:
                    totalBananas += 1
                    dq.append([i,j, 0])
        
        minutes = 0

        while dq:
            i, j, time = dq.popleft()
            

            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or (i,j) in seen:
                pass
            else:
                minutes = max(minutes, time)
                seen.add((i,j))
                grid[i][j] = 2
                rottenBananas += 1
                dq.append([i-1,j,time+1])
                dq.append([i+1,j,time+1])
                dq.append([i,j+1,time+1])
                dq.append([i,j-1,time+1])


        return minutes if totalBananas == rottenBananas else -1