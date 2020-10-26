#Function to print the permutation of a given input string

#function inputs a string as list, the start location and the end location
def stringPermute(per,a,b):
    if a==b:
        print("".join(string))
    else:
        for i in range(a,b+1):
            per[a], per[i] = per[i], per[a] 
            stringPermute(per, a+1, b) 
            per[a], per[i] = per[i], per[a]

string="GIT"  #give input string
init_index=0  #initial index
last_index=len(string)-1  #index of last element
stringPermute(list(string),init_index,last_index) 