def get_factors(x):
    factors = list()
    for i in range(1, x+1):
       if x % i == 0:
           factors.append(i)
    return(factors)


def get_factors_in_range(x,min_factor, max_factor):
    factors = list()
    for i in range(min_factor, max_factor+1):
       if x % i == 0:
           factors.append(i)
    return(factors)

def get_paired_factors_in_range(num, min_factor, max_factor):
    paired_factors = set()
    # get_factors to get all od the factors
    factors = get_factors_in_range(num, min_factor, max_factor)
    # use doulble loop to find all pairs
    for factor_a in factors:
        for factor_b in factors:
            product = factor_a * factor_b
            if product == num:
                paired_factors.add((factor_a, factor_b))
    return(paired_factors)


def smallest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("Min greater than max")
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
            for factor_a in get_factors_in_range(i,min_factor, max_factor):
                for factor_b in get_factors_in_range(i,min_factor, max_factor):
                    product = factor_a * factor_b
                    if product == i:
                        return(i)
    smallest_palindrome = get_smallest_palindrome(max_factor, min_factor)
    if smallest_palindrome is None:
        return([None, list()])
    product_pairs = get_paired_factors_in_range(smallest_palindrome, min_factor, max_factor)
    return([smallest_palindrome, product_pairs])

def largest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("Min greater than max")
    def get_largest_palindrome(max_factor, min_factor):
        min_product = min_factor ** 2
        max_product = max_factor ** 2
        # Find the minimum palindrone
        # go between th min and max product 
        for i in range(max_product,min_product-1, -1):
            # if the number id not a palindrone, then next
            if str(i)[::-1] != str(i):
                continue
            # if the number is a palindrone, then we'll see if we can get a paired factor within range
            # get the products for i and then use a doulble loop to find paired factors
            for factor_a in get_factors_in_range(i,min_factor, max_factor):
                for factor_b in get_factors_in_range(i,min_factor, max_factor):
                    product = factor_a * factor_b
                    if product == i:
                        return(i)
    largest_palindrome = get_largest_palindrome(max_factor, min_factor)
    if largest_palindrome is None:
        return([None, list()])
    product_pairs = get_paired_factors_in_range(largest_palindrome, min_factor, max_factor)
    return([largest_palindrome, product_pairs])