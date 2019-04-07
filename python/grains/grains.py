def on_square(integer_number):
    
    if integer_number <= 0:
        raise ValueError("Can't have 0 or negatives")

    if integer_number > 64:
        raise ValueError("Can't have more than 64 squares")

    grains = 1

    for i in range(1,integer_number):
        grains = grains * 2
    
    return(grains)



def total_after(integer_number):
    if integer_number <= 0:
        raise ValueError("Can't have 0 or negatives")
    
    if integer_number > 64:
        raise ValueError("Can't have more than 64 squares")

    sum = 0 

    for i in range(1,integer_number+1):
        print(i)
        sum += on_square(i)

    return(sum)
