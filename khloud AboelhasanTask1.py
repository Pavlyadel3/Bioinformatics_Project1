#كاترين اشرف عادل زكي 20191701143
#خلود ابوالحسن عبدالبديع محمد زين 20191701066
#ريهام عصام جمال المتولى 20191701087
#روان احمد السيد محمد 20191701077
#اندرو امير فوزى صموئيل 20191701038
#بافلى عادل ابراهيم فام 20191701048

dictionary = {156: 'R', 114: 'N', 115: 'D', 103: 'C', 129: 'E', 128: 'K', 57: 'G', 137: 'H', 113: 'L', 131: 'M', 147: 'F', 97: 'P', 87: 'S', 101: 'T', 186: 'W', 163: 'Y', 99: 'V', 71: 'A'}
print("Weight.txt:",dictionary)
spectrum = [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]
print("Spectrum:",spectrum)

def initial_list(dictionary, spectrum): #loop over dictionary & spectrum to get the aa that will be used in formation of peptide and put it into the initial list
    initallist = []
    for i in spectrum:
        for key, value in dictionary.items():
            if i == key and key < 186:
                initallist.append(value)
    print("Initial_list:",initallist)
    return initallist

def linear_spectrum(sub_peptide, dict): #loop over dictionary given sub_peptide resulted from each combination to get its weight
    total = []
    weight = 0
    for i in sub_peptide:
        for key, value in dict.items():
            if i == value:
                #total.append(key)  #this line to put weight of each aa too, to be used in condition of avoiding repeatition
                weight += key
    total.append(weight)
    return total

def counted_letters(spectrum): #loop over given spectrum to take its weight and number of its occurencein list
    c = {}
    for i in spectrum:
        c[i] = spectrum.count(i)
    return c

def is_consistent(spectrum, sub_peptide): #check if the peptide is consistent to be used in following combinations (weight/repeatition of aa)
    values = linear_spectrum(sub_peptide, dictionary)
    counts = counted_letters(spectrum)
    counter = 0
    for i in values:                      #available part for checking weight and commented part should have checked repeatition of each aa allowed or not
        for j in range(len(spectrum)):
            if spectrum[j] == i:
                # for key, value in counts.items():
                #     if i == key:  # 97==97
                #         counter += 1
                #         if counter <= value:  # counter <= number of occurrence of weight
                #             found = True
                return True
                break
            else:
                continue
    return False
#Weights are calculated correctly but the condition of "Is consistent" is not working properly so the final output may contain some repetitions

def creating_combination_lists(initlist, input_list, output_comblist): #loop over lists and create combinations of 2_mer,3_mer,and so on until finishing length of initial list
    for k in range(len(input_list) - 1):
        for i in input_list:
            for j in initlist:
                peptide = i + j
                found = is_consistent(spectrum, peptide)
                if (found == True) and output_comblist.count(peptide) == 0:
                    output_comblist.append(peptide)
        input_list = output_comblist.copy()
        output_comblist.clear()
        print("List",k+2,"_mer:",input_list) #print lists of consistents (acc to weight) + other consistents peptides resulted due to repeatition problem
    print("#FINAL_LIST_OF_POSSIBLE_PEPTIDES:#")
    return input_list

# Main For Calling Functions
list = initial_list(dictionary, spectrum)
combination_list = []
l = creating_combination_lists(list, list, combination_list)
print(l)

#it calls function of creating initial list and enter function of creating combination lists with it as a starter.
#on creating each combination function is consistent is called to check it which btw call function linear spectrum and count to check by weight and repeated parts