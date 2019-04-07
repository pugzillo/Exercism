def get_factors(x):
    factors = list()
    for i in range(1, x + 1):
       if x % i == 0:
           factors.append(i)
    return(factors)

def get_paired_factors_in_range(num, min_factor, max_factor):
    paired_factors = set()
    # get_factors to get all od the factors
    factors = get_factors(num)
    # use doulble loop to find all pairs
    for factor_a in factors:
        for factor_b in factors:
            product = factor_a * factor_b
            if product == num:
                paired_factors.add((factor_a, factor_b))
    return(paired_factors)

def products(max_factor, min_factor):
    product_dict = dict()   # Dict with all products for min and max


    min_product = min_factor ** 2
    max_product = max_factor ** 2
    # Find the minimum palindrone
    # go between th min and max product 
    for i in range(min_factor,max_factor+1):
        # if the number id not a palindrone, then next
        if str(i)[::-1] != str(i):
            continue
        # if the number is a palindrone, then we'll see if we can get a paired factor within range
        # get the products for i and then use a doulble loop to find paired factors
        for factor_a in get_factors(i):
            for factor_b in get_factors(i):
                product = factor_a * factor_b



        # separately find the max palindrone 


        

    # for each palindrone, Get all of the factors from min to max, inclusive and then find pairs


    for i in range(min_factor,max_factor+1):
        print(i)
        for j in range(min_factor, max_factor+1):
            print(j)
            if i*j not in product_dict:
                product_dict[i*j] = [(i,j)]
            else:
                product_dict[i*j].append((i,j))

    palidrones_idx = dict() # Dict with palindrome products
    for product in product_dict:
        print(product)
        if str(product)[::-1] == str(product):
            palidrones_idx[product] = product_dict[product]

    return(palidrones_idx)

def largest_palindrome(max_factor, min_factor):
    product_palindromes = products(max_factor, min_factor)
    pp_max = max(list(product_palindromes.keys()))

    largest_palindrome_list = list()
    for i in product_palindromes:
        if i == pp_max:
            for i in product_palindromes[i]:
                largest_palindrome_list.append(i)

    factors = set(largest_palindrome_list)
    first_factors = next(iter(factors))
    value = first_factors[0] * first_factors[1]
    return(
        [
            value,
            factors
        ]
    )

# def smallest_palindrome(max_factor, min_factor):
#     # product_palindromes = products(max_factor, min_factor)
#     # pp_list = list(product_palindromes.keys())

#     # factors = set(product_palindromes[min(pp_list)])
#     # first_factors = next(iter(factors))
#     # value = first_factors[0] * first_factors[1]
#     # return(
#     #     [
#     #         value,
#     #         factors
#     #     ]
#     # )

def smallest_palindrome(max_factor, min_factor):
    def get_smallest_palindrome(max_factor, min_factor):
        min_product = min_factor ** 2
        max_product = max_factor ** 2
        # Find the minimum palindrone
        # go between th min and max product 
        for i in range(min_product,max_product+1):
            # if the number id not a palindrone, then next
            if str(i)[::-1] != str(i):
                continue
            # if the number is a palindrone, then we'll see if we can get a paired factor within range
            # get the products for i and then use a doulble loop to find paired factors
            for factor_a in get_factors(i):
                for factor_b in get_factors(i):
                    product = factor_a * factor_b
                    if product == i:
                        return(i)
    smallest_palindrome = get_smallest_palindrome(max_factor, min_factor)
    if smallest_palindrome is None:
        return([None, list()])
    product_pairs = get_paired_factors_in_range(smallest_palindrome, min_factor, max_factor)
    return([smallest_palindrome, product_pairs])
