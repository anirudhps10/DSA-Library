#Function to print the permutation of a given input string

#function inputs a string as list, the start location and the end location
def stringPermute(string,a,b):
    if a==b:
        print("".join(string))
    else:
        for i in range(a,b+1):
            str[a], str[i] = str[i], str[a] 
            stringPermute(, a+1, b) 
            str[a], str[i] = str[i], str[a]

string="GIT"  #give input string
init_index=0  #initial index
last_index=len(string)-1  #index of last element
stringPermute(list(string),init_index,last_index) 