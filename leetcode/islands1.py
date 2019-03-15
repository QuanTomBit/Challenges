class Solution(object):

    islands = 0
    q = []
    v = {} # 1 - self.visited; 0 - not self.visited
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # if not visited and is land
                if self.v.setdefault((i, j), 0) == 0 and grid[i][j] == "1":
                    self.islandsBFS(grid, i, j)
                    self.islands += 1
                    print("ISLANDS")
        return self.islands
    def islandsBFS(self, grid, i, j):
        self.q.append((i, j))
        self.v[(i, j)] = 1
        length = len(grid)
        while not len(self.q) == 0:
            size = len(self.q)
            if length > 1:
                for s in range(size):
                    i, j = self.q.pop(0)
                    if len(grid[i]) > 1:
                        if i == 0: # top edge
                            if j == 0: # left edge
                                if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                    self.q.append((i, j + 1))
                                    self.v[(i, j + 1)] = 1
                                if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                    self.q.append((i + 1, j))
                                    self.v[(i + 1, j)] = 1
                            elif j == len(grid[i]) - 1: # right edge
                                if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                    self.q.append((i, j - 1))
                                    self.v[(i, j - 1)] = 1
                                if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                    self.q.append((i + 1, j))
                                    self.v[(i + 1, j)] = 1
                            else: # middle
                                if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                    self.q.append((i, j + 1))
                                    self.v[(i, j + 1)] = 1
                                if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                    self.q.append((i + 1, j))
                                    self.v[(i + 1, j)] = 1
                                if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                    self.q.append((i, j - 1))
                                    self.v[(i, j - 1)] = 1
                        elif i == len(grid) - 1: # bottom edge
                            if j == 0: # left edge
                                if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                    self.q.append((i, j + 1))
                                    self.v[(i, j + 1)] = 1
                                if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                    self.q.append((i - 1, j))
                                    self.v[(i - 1, j)] = 1
                            elif j == len(grid[i]) - 1: # right edge
                                if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                    self.q.append((i, j - 1))
                                    self.v[(i, j - 1)] = 1
                                if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                    self.q.append((i - 1, j))
                                    self.v[(i - 1, j)] = 1
                            else: # middle
                                if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                    self.q.append((i, j + 1))
                                    self.v[(i, j + 1)] = 1
                                if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                    self.q.append((i - 1, j))
                                    self.v[(i - 1, j)] = 1
                                if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                    self.q.append((i, j - 1))
                                    self.v[(i, j - 1)] = 1
                        else: # middle
                            if j == 0: # left edge
                                if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                    self.q.append((i, j + 1))
                                    self.v[(i, j + 1)] = 1
                                if self.v.setdefault((i -1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                    self.q.append((i - 1, j))
                                    self.v[(i - 1, j)] = 1
                                if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                    self.q.append((i + 1, j))
                                    self.v[(i + 1, j)] = 1
                            elif j == len(grid[i]) - 1: # right edge
                                if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                    self.q.append((i, j - 1))
                                    self.v[(i, j - 1)] = 1
                                if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                    self.q.append((i - 1, j))
                                    self.v[(i - 1, j)] = 1
                                if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                    self.q.append((i + 1, j))
                                    self.v[(i + 1, j)] = 1=
                            else: # middle
                                if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                    self.q.append((i, j + 1))
                                    self.v[(i, j + 1)] = 1
                                if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                    self.q.append((i - 1, j))
                                    self.v[(i - 1, j)] = 1
                                if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                    self.q.append((i, j - 1))
                                    self.v[(i, j - 1)] = 1
                                if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                    self.q.append((i + 1, j))
                                    self.v[(i + 1, j)] = 1
                    elif len(grid[i]) == 1: # multiple rows of single cells
                        if i == 0: # top edge
                            if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                self.q.append((i + 1, j))
                                self.v[(i + 1, j)] = 1
                        elif i == len(grid) - 1: # bottom edge
                            if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                self.q.append((i - 1, j))
                                self.v[(i - 1, j)] = 1
                        else: # middle
                            if self.v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == "1": # North neighbor
                                self.q.append((i - 1, j))
                                self.v[(i - 1, j)] = 1
                            if self.v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == "1": # South neighbor
                                self.q.append((i + 1, j))
                                self.v[(i + 1, j)] = 1
            elif length == 1: # grid is single row
                for s in range(length):
                    i, j = self.q.pop(0)
                    if len(grid[i]) > 1: # grid is single cell
                        if j == 0: # left edge
                            if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                self.q.append((i, j - 1))
                                self.v[(i, j - 1)] = 1
                        elif j == len(grid[i]) - 1: # right edge
                            if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                self.q.append((i, j - 1))
                                self.v[(i, j - 1)] = 1
                        else: # middle
                            if self.v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == "1": # East neighbor
                                self.q.append((i, j + 1))
                                self.v[(i, j + 1)] = 1
                            if self.v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == "1": # West neighbor
                                self.q.append((i, j - 1))
                                self.v[(i, j - 1)] = 1
