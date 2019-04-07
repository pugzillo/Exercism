def is_pangram(sentence):
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")   # tuple of alphabet
    
    state = True    # Whether or not sentence is panagram
    
    for x in alphabet:
        if x in sentence.lower():
            continue
        else:
            state = False

    return(state)
