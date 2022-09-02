#Problem 81 from CodeAbbey website

def bit_count(repeatitions):

    num_list = [] #list to collect the input

    for _ in range(repeatitions):
        
        x = int(input("Provide numbers to be bit-counted: "))
        num_list.append(bin(x)[2:])
    
    print(f'Binary version of number list is {num_list}')
    ones_list = []


    for bins in num_list:
        one_count = 0
        for number in bins:
            if number == "1":
                one_count += 1
        ones_list.append(one_count)

    return ones_list