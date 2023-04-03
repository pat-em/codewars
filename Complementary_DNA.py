def DNA_strand(dna):

    dna_comp_side = ""
    
    for i in dna:
        if i == "A":
            dna_comp_side += "T"
        if i == "T":
            dna_comp_side += "A"
        if i == "C":
            dna_comp_side += "G"
        if i == "G":
            dna_comp_side += "C"

    return dna_comp_side

#lepsze rozwiązanie 1
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

#lepsze rozwiąznie 2:
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])