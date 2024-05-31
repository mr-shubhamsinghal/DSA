
from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:

        r = len(grid)
        c = len(grid[0])
        perimeter = 0

        for i in range(r):
            for j in range(c):

                if grid[i][j]:
                    # top
                    if i-1 < 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # right
                    if j+1 >= c or grid[i][j+1] == 0:
                        perimeter += 1
                    # bottom
                    if i+1 >= r or grid[i+1][j] == 0:
                        perimeter += 1
                    # left
                    if j-1 < 0 or grid[i][j-1] == 0:
                        perimeter += 1
        
        return perimeter

if __name__ == "__main__":
     grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
     print(islandPerimeter(grid))