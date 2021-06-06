#creating the function 
def to_reverse(list):
    actual_string=""
    list.reverse()
    for i in range(len(list)):
        actual_string+=str(list[i])
    return [list,actual_string]
