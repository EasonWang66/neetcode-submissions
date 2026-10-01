class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # 越界，或者当前位置是水，就停止
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or grid[r][c] == "0"
            ):
                return

            # 标记这块陆地已访问
            grid[r][c] = "0"

            # 继续探索四个方向
            dfs(r - 1, c)  # 上
            dfs(r + 1, c)  # 下
            dfs(r, c - 1)  # 左
            dfs(r, c + 1)  # 右

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands