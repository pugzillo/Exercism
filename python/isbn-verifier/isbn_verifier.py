import re

# Checks for isbn validity

def verify(isbn):
    isbn = isbn.replace("-", "")

    # CHecks length of isbn
    if len(isbn) != 10:
        return(False)

    loops = 10  
    counter = 0

    for i in isbn:
        if i not in list(str(j) for j in range(10)) + ['X']: # Checks for invalid characters
            return(False)

        if i == 'X': # CHeck for X at the end
            if loops == 1:
                i = 10
            else: 
                return(False)

        counter += int(i) * loops
        loops -= 1

    if counter % 11 == 0:
        return(True)
    else:
        return(False)


