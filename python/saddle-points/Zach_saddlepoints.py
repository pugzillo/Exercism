def saddle_points(matrix):
    # find the max values per row and store index of row and col position
    def find_row_maxes(matrix):
    # find the min per column and store the index of row and col position
        row_maxes = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val is max(row):
                    row_maxes.append((i + 1, j + 1))
        return row_maxes
    def find_col_mins(matrix):
        col_mins = []
        for i, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                col = list(
                    map(
                        lambda row: row[col_idx],
                        matrix
                    )
                )
                if val is min(col):
                    col_mins.append((i + 1, col_idx + 1))
        return col_mins
    # find overlap
    row_maxes = find_row_maxes(matrix)
    col_mins = find_col_mins(matrix)
    return set(row_maxes) & set(col_mins)
