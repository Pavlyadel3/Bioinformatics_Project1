file = open("weight.txt")
aadict={}
# read weights file and save data in dictionary
for f in file:
    line= f.rstrip()
    words=line.split(" ")
    aa = words[0]
    w = int(words[1])
    aadict[aa]=w

#function that return the theortical spectrum
def theoritical(peptide):
    sublist=[peptide]
    for i in range(len(peptide)):
        for j in range(len(peptide)):
            if (i+j)< len(peptide):
                 sublist.append(peptide[j:j+i+1])
            else:
                sublist.append(peptide[j:len(peptide)]+peptide[0:(i+j)-len(peptide)])

    totals = [0]
    #loop calculate weights for each element in the list
    for i in sublist:
            totals.append(weight(i))
    # the totals list must be sorted
    sortedTotals=sorted(totals)
    return sortedTotals

#function take each element in the sublist to calculate the weight
def weight(subpeptide):
    total=0
    for s in subpeptide:
        total+=aadict[s]
    return total

#Main
peptide = input("Enter the Peptide: ")
print(theoritical(peptide))