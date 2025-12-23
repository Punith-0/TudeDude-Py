def sun():

    print("The sum of numbers from 1 to 50 is" ,sum( n for n in range(51)))

def sun1() :
    sum  = 0 
    for _ in range(51):
        sum += _
    print(sum)

sun()
sun1()