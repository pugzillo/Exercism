def proteins(strand):
    translation = {
        "AUG":"Methionine", 
        "UUU":"Phenylalanine", 
        "UUC":"Phenylalanine", 
        "UUA":"Leucine",
        "UUG":"Leucine",
        "UCU":"Serine",
        "UCC":"Serine",
        "UCA":"Serine",
        "UCG":"Serine",
        "UAU":"Tyrosine",
        "UAC":"Tyrosine",
        "UGU":"Cysteine",
        "UGC":"Cysteine",
        "UGG":"Tryptophan",
        "UAA":"STOP",
        "UAG":"STOP",
        "UGA":"STOP"
    }

    protein = list()

    num_loops = int(len(strand) / 3)

    if len(strand) % 3 == 0:
        for num in range(num_loops):
            start = num * 3
            end = start + 3 # triplets
            codon = strand[start:end]
            print(codon)
            if translation[codon] == "STOP":
                break
            else:
                protein.append(translation[codon])

    else: 
        return ValueError("RNA bases not divisible by 3.")

    return(protein)