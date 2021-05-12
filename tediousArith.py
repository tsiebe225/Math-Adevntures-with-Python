def average(listNums):
    return sum(listNums)/len(listNums)

def mySum(end):
    runningsum = 0
    for i in range(1, end+1):
        runningsum += i
    return runningsum

def mySum2(end):
    runningSum = 0
    for i in range( end +1):
        runningSum += i*i+1
    return  runningSum

l1=[234324,234234,464641313,3143434,3434189684,347981,4196471,-46763149,-4347467]

print(average(l1))

print(mySum(100))

print(mySum2(20))

print(mySum(100)) #50 pairs of 100 plus mid of 50
print(mySum(1000)) #50 pairs of 1000 plus the mid of 500