def and_Gate(Upperbit,Lowerbit):
    if Upperbit==1 and Lowerbit==1:
        return 1
    else:
        return 0
def or_Gate(Upperbit,Lowerbit):
    if Upperbit==1:
        return 1
    elif Lowerbit==1:
        return 1
    else:
        return 0
def compliment_gate(bit):
    if bit==0:
        return 1
    elif bit==1:
        return 0
'''ef and_Gate(Upperbit,Lowerbit):
    return Upperbit& Lowerbit
def or_Gate(Upperbit,Lowerbit):
    return Upperbit | Lowerbit
def compliment_gate(bit):
    return ~bit'''
def xor_Gate(Upperbit,Lowerbit):
    a=and_Gate(compliment_gate(Upperbit),Lowerbit)
    b=and_Gate(Upperbit,compliment_gate(Lowerbit))
    c=or_Gate(a,b)
    return int(c)
def to_carry(Upperbit,Lowerbit,carry):
    a1=xor_Gate(Upperbit,Lowerbit)
    b1=and_Gate(Upperbit,Lowerbit)
    c1=and_Gate(carry,a1)
    d1=or_Gate(c1,b1)
    return int(d1)
def calculate_result(Upperbit,Lowerbit):
    result=[]
    carry=0
    Upperbit.reverse()
    Lowerbit.reverse()
    for i in range(len(Upperbit)):
        sum1=xor_Gate(Upperbit[i],Lowerbit[i])
        result.append(xor_Gate(sum1,carry))
        carry=to_carry(Upperbit[i],Lowerbit[i],carry)
        i+=1
    result.append(carry)
    return result
