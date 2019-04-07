def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands don't have matching lengths!")
    
    hamming = 0

    for i in range(len(strand_a)):
        if list(strand_a)[i] != list(strand_b)[i]:
            hamming += 1 
    
    return(hamming)
