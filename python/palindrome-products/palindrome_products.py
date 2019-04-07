def products(max_factor, min_factor):
    product_dict = dict()   # Dict with all products for min and max
    
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

def smallest_palindrome(max_factor, min_factor):
    product_palindromes = products(max_factor, min_factor)
    pp_list = list(product_palindromes.keys())

    factors = set(product_palindromes[min(pp_list)])
    first_factors = next(iter(factors))
    value = first_factors[0] * first_factors[1]
    return(
        [
            value,
            factors
        ]
    )
