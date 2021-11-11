# https://leetcode.com/problems/number-of-islands/submissions/
class NumIslands:

    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or len(grid)-1 < i or len(grid[i])-1 < j or grid[i][j] != "1":
            return

        grid[i][j] = "$"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)

    def dfsSum(self, grid, s, i, j):
        if i < 0 or j < 0 or len(grid)-1 < i or len(grid[i])-1 < j or grid[i][j] != 1:
            return s

        grid[i][j] = "$"
        s += 1
        s = self.dfsSum(grid, s, i+1, j)
        s = self.dfsSum(grid, s, i, j+1)
        s = self.dfsSum(grid, s, i-1, j)
        s = self.dfsSum(grid, s, i, j-1)

        return s

# https://leetcode.com/problems/max-area-of-island/
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mx = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mx = max(mx, self.dfsSum(grid, 0, i, j))
        return mx


if __name__ == "__main__":
    n = NumIslands()
    print(n.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
          0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
