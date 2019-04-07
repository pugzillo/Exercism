def find_anagrams(word, candidates):
    word_dict = {}

    # Dict with letters as key and letter count as vals
    for i in list(word.upper()):
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    
    anagrams = list()

    # Make Dict for each candidate and compare to word dict
    for i in candidates:
        if i.upper() == word.upper():   # No self anagrams
            continue

        temp_list = list(i.upper())

        temp_dict = {}

        for j in temp_list:
            if j in temp_dict:
                temp_dict[j] += 1
            else:
                temp_dict[j] = 1
        
        if word_dict == temp_dict:  # Compare candidate word and input word
            anagrams.append(i)

    return(anagrams)


