from numpy import * 

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def split_to_matrix(self):
        row_str = self.matrix_string.split('\n')
        a = list()
        x = 0
        
        for i in row_str:
            val = i.split()    # split row str into a list
            temp_list = [int(x) for x in val]    # convert strs into ints
            a = append(a, temp_list) # append to array
            if len(i.split()) > x:  #   widest column
                x = len(i.split())

        y = len(row_str)    # number of rows
        return(reshape(a,(y,x)))
    
    def row(self, index):
        position = index - 1
        res = self.split_to_matrix()[position]
        return(list(res))
        # return([3.0, 4.0])

    def column(self, index):
        position = index - 1
        res = [row[position] for row in self.split_to_matrix()]
        return(list(res))
