def saddle_points(matrix):
    # find the max values per row and store index of row and col position
    def find_row_maxes(matrix):

    # find the min per column and store the index of row and col position
    def find_col_mins(matrix):

    # find overlap
    row_maxes = print(find_row_maxes(matrix))
    col_mins = print(find_col_mins(matrix))
    return set(row_maxes) & set(col_mins)
