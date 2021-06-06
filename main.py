
import calculation
import validation
import reverse
import conversion


def to_check_number():
    while True:
        number=int(validation.validation())
        if (number>0 and number<256):
            print("Thank you for the values ")
            break
        else:
            print("Please enter numbers between 0-256")
            continue
    return number
def main_method():
    while True:
        print(("\n"))
        numbera=to_check_number()
        print("The first number is:",numbera,)
        binary_numbera=conversion.to_convert(numbera)
        actual_binarya=reverse.to_reverse(binary_numbera)
        print("The conversion of number in  binary list is :",actual_binarya[1])
        print("The binary number is:",actual_binarya[0])
        numberb=to_check_number()
        print("The second number is:",numberb)  
        binary_numberb=conversion.to_convert(numberb)
        actual_binary=reverse.to_reverse(binary_numberb)
        print("The conversion of number in binary list is :",actual_binary[0])
        print("The binary number is:",actual_binary[1])
        reverse_result=calculation.calculate_result(actual_binary[0],actual_binary[0])
        actual_result=reverse.to_reverse(reverse_result)
        print("The sum of numbers in binary in list is:",actual_result[0])
        print("The sum of the number in binary  is:",actual_result[1])
        print(("\n"))
        continuos=input("DO you wish to continue ?(Y?N)")
        if continuos.upper()=="Y":
            continue
        elif continuos.upper()=="N":
            break
        
if __name__=='__main__':
    main_method()

  

