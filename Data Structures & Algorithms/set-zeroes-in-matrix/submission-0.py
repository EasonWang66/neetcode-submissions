class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        if not matrix or not matrix[0]:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # 1. 记录第一行、第一列原本是否有 0
        first_row_zero = any(
            matrix[0][c] == 0 for c in range(cols)
        )
        first_col_zero = any(
            matrix[r][0] == 0 for r in range(rows)
        )

        # 2. 用第一行、第一列记录内部的 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 3. 根据标记，把内部元素清零
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 4. 最后处理第一行、第一列
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0