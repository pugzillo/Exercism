def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands don't have matching lengths!")
    
    # hamming = sum(tpl[0] != tpl[1] for tpl in zip(strand_a, strand_b))

    hamming = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming += 1 
    
    return(hamming)
