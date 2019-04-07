# def to_rna(dna_strand):
#     rna_strand = str()

#     for i in list(dna_strand):
#         ribonuc = str()
        
#         if i == "G":
#             ribonuc = "C"
#         elif i == "C":
#             ribonuc = "G"
#         elif i == "T":
#             ribonuc = "A"
#         elif i == "A":
#             ribonuc = "U"
#         else:
#             continue
        
#         rna_strand += ribonuc

#     return(rna_strand)
    

def to_rna(dna_strand):
    transcription = {
        "G":"C", 
        "C":"G", 
        "T":"A", 
        "A":"U"
    }
    rna_strand = str()

    for i in list(dna_strand):
        rna_strand += transcription[i]
    
    return(rna_strand)


