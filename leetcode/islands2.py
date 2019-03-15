class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0 # will hold total number of islands
        v = {} # will hold info on if an island was visited int(1) or not int(0)
        grid_len = len(grid)
        if grid_len < 1: # if empty grid
            return 0
        for i in range(grid_len):
            grid[i].insert(0, u'0') # western edge
            grid[i].append(u'0') # eastern edge
        grid.insert(0, [u'0'] * len(grid[0])) # northern edge
        grid.append([u'0'] * len(grid[grid_len - 1])) # southern edge
        grid_len = len(grid)
        row_len = len(grid[0])
        for i in range(1, grid_len - 1):
            for j in range(1, row_len - 1): # len(grid[i]) - 1 unnecessary for this problem (grid is always square)
                if v.setdefault((i, j), 0) == 0 and grid[i][j] == u'1':
                    self.islandsBFS(grid, v, i, j) # find rest of island and mark cells as visited
                    islands += 1
        return islands
    def islandsBFS(self, grid, v, i, j):
        q = []
        q.append((i, j)) # insert root cell into queue
        v[(i, j)] = 1 # mark root cell as visited
        while not len(q) == 0:
            q_len = len(q)
            for x in range(q_len):
                i, j = q.pop(0)
                if v.setdefault((i - 1, j), 0) == 0 and grid[i - 1][j] == u'1': # North neighbor
                    v[(i - 1, j)] = 1
                    q.append((i - 1, j))
                if v.setdefault((i + 1, j), 0) == 0 and grid[i + 1][j] == u'1': # South neighbor
                    v[(i + 1, j)] = 1
                    q.append((i + 1, j))
                if v.setdefault((i, j - 1), 0) == 0 and grid[i][j - 1] == u'1': # West neighbor
                    v[(i, j - 1)] = 1
                    q.append((i, j - 1))
                if v.setdefault((i, j + 1), 0) == 0 and grid[i][j + 1] == u'1': # East neighbor
                    v[(i, j + 1)] = 1
                    q.append((i, j + 1))
