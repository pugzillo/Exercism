def get_factors_in_range(x,min_factor, max_factor):
    factors = list()
    for i in range(min_factor, max_factor+1):
       if x % i == 0:
           factors.append(i)
    return(factors)

def get_paired_factors_in_range(num, min_factor, max_factor):
    """
    Two numbers that multiply to a specific number (ie. 2 and 3 are factors of 6. Also 1 and 6)
    """
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

def get_extreme_palindrome(max_factor, min_factor, min_or_max):
        min_product = min_factor ** 2
        max_product = max_factor ** 2
        # Find the minimum palindrone
        # go between th min and max product
        range_args = [
            min_product,
            max_product + 1
        ] if min_or_max is 'min' else [
            max_product,
            min_product - 1,
            -1
        ]
        for candidate_for_extreme_palindrome in range(*range_args):
            # if the number id not a palindrone, then next
            if str(candidate_for_extreme_palindrome)[::-1] != str(candidate_for_extreme_palindrome):
                continue
            # if the number is a palindrone, then we'll see if we can get a paired factor within range
            # get the products for i and then use a doulble loop to find paired factors
            factors = get_factors_in_range(candidate_for_extreme_palindrome,min_factor, max_factor)
            for factor_a in factors:
                for factor_b in factors:
                    product = factor_a * factor_b
                    if product == candidate_for_extreme_palindrome:
                        return(candidate_for_extreme_palindrome)


def smallest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("Min greater than max")
    smallest_palindrome = get_extreme_palindrome(max_factor, min_factor, "min")
    if smallest_palindrome is None:
        return([None, list()])
    product_pairs = get_paired_factors_in_range(smallest_palindrome, min_factor, max_factor)
    return([smallest_palindrome, product_pairs])

def largest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("Min greater than max")
    largest_palindrome = get_extreme_palindrome(max_factor, min_factor, "max")
    if largest_palindrome is None:
        return([None, list()])
    product_pairs = get_paired_factors_in_range(largest_palindrome, min_factor, max_factor)
    return([largest_palindrome, product_pairs])
