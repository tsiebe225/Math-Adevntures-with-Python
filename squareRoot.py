def average(a,b):
    return (a+b)/2

def squareRoot(num,low,high):
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num:
            high = guess
        else:
            low = guess
    print(guess)



squareRoot(50000,223,224)