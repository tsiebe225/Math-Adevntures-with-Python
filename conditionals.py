def factors(num):
    factorList = []
    for i in range(1,num+1):
        if num % i == 0:
            factorList.append(i)
    return  factorList

def cf(num1, num2):
    num1FactorList = factors(num1)
    num2FactorList = factors(num2)
    cfList = []
    for item in num1FactorList:
        if item in num2FactorList:
            cfList.append(item)
    return cfList

def gcf(num1,num2):
    cfList = cf(num1,num2)
    return  cfList[-1]

print(factors(1768))
print(gcf(150,138))