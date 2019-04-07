def is_armstrong(number):
    numlist = [int(d) for d in str(number)]
    sum = 0
    for i in numlist:
        sum += i**len(numlist)
    if sum == int(number):
        return(True)
    else:
        return(False)

