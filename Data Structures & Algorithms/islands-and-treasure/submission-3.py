class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        searcher = [] # (i, j, x)
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    searcher.append((i,j,0))

        for i, j, x in searcher:
            if i < 0 or i >= n or j < 0 or j>= m:
                pass
            elif x != 0 and (grid[i][j] == -1 or grid[i][j] <= x): 
                pass
            else:
                grid[i][j] = x 
                searcher.append((i+1,j,x+1))
                searcher.append((i-1,j,x+1))
                searcher.append((i,j+1,x+1))
                searcher.append((i,j-1,x+1))
