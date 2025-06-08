class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])        

        low = 0
        high = m * n - 1
        while low <= high:
            pivot_idx = low + (high - low) // 2
            mid = matrix[pivot_idx // n][pivot_idx % n]
            if mid == target:
                return True
            elif mid < target:
                low = pivot_idx + 1
            else:
                high = pivot_idx - 1
        return False
    
# General Mapping Rule
# If the matrix has n columns (here n = 4), then for any 1D index k:

# Row (i): k // n → divides index by number of columns to get row

# Column (j): k % n → gives remainder (what’s left in that row)

# Let’s see a few examples:

# 1D index k	k // 4 = row	k % 4 = col	matrix[row][col]
# 0	0	0	0
# 3	0	3	3
# 4	1	0	4
# 7	1	3	7
# 10	2	2	10

# Why it works:
# Think of the 1D index k as "how far" you’ve moved from the start.

# Every full n steps (n columns) moves you 1 row down → that’s why k // n gives the row.

# Whatever is left after those full rows is the column within that row → that's k % n.