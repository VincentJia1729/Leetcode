class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # a row of all 1's

        for i in range(m-1): # 1 less than the number of rows
            new_row = [1] * n # another row of 1's
            for j in range(n-2, -1, -1): # "n-2" to account for 0 indexing. loops 1 less than the num of cols
                new_row[j] = new_row[j+1] + row[j] # new_row[j+1] for j = n-2 will always be 1
            row = new_row
        return row[0]