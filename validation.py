#creating the function validation
def validation():
    #expectinal handling is done inside while loop 
    while True:
        try:
            num=int(input("Enter the Numbers:")) 
        except ValueError:
            print("Please enter number only")
            continue
        else:
            break
    return num
