#creating the function
def to_convert(number):
    reversed_binary=[] 
    
    for i in range(1,9,1):
        remainder=number%2
        reversed_binary.append(remainder)
        number=number//2
        i+=1
    return reversed_binary
