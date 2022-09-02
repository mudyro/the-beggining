#Problem 81 from CodeAbbey website

def bit_count(repeatitions): #Enter how many numbers you want to check

    num_list = [] #list to collect the input

    for _ in range(repeatitions): # convert the numbers into binary
        
        x = int(input("Provide numbers to be bit-counted: "))
        num_list.append(bin(x)[2:])
    
    print(f'Binary version of number list is {num_list}') #Show the binary representation of the list
    ones_list = [] 
    
    for bins in num_list: #now count how many ones are there in each number binary representation and collect them into list (dictionary prolly would be better as i now think)
        one_count = 0
        for number in bins:
            if number == "1":
                one_count += 1
        ones_list.append(one_count)
    
    #actually lets make them dictionaries
    pairs = []
    for i in range(len(num_list)):
        pair = {num_list[i]:ones_list[i]}
        pairs.append(pair)
    return pairs
