def DNA_strand(dna):
    dicti = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    l = []
    l1 = []
    finalString = '';
    
    for i in range(0, len(dna)):
        l.append(dna[i])
        
    for j in range(0, len(l)):
        l1.append(dicti[l[j]])
        
    for k in range(0, len(l1)):
        finalString += l1[k]
    
    return finalString