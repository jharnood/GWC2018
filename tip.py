total= input("How much was your meal?")

def tipcalculator (bill, percent):
    answer= (bill*percent)
    return answer
final= tipcalculator(float(total),.15)
print(" Your tip is $",final)
