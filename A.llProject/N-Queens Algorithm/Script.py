def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def is_valid(solution, row, col):
        for r in range(row):
            # same column
            if solution[r] == col:
                return False
            # same diagonal
            if abs(solution[r] - col) == abs(r - row):
                return False
        return True

    def dfs(row, solution):
        # base case: all rows filled
        if row == n:
            solutions.append(solution.copy())
            return

        # try every column in this row
        for col in range(n): 
            #is_valid check if any Q in the same row,colomn,and diagnoal
            if is_valid(solution, row, col):
                solution.append(col)     # choose
                #explore each row that 
                dfs(row + 1, solution)   # explore
                solution.pop()           # backtrack

    dfs(0, [])
    return solutions


dfs_n_queens(4)