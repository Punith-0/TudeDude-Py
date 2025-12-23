import math as m 

def mathdis(num :int) :
    print(f"Square root  : {m.sqrt(num)}")
    print(f"logarithmic : {m.log(num).__round__(2)}")
    print(f"Sine : {m.sin(num)}")
          
def main() :
    num : int = int(input("Enter a number : "))
    mathdis(num)

main()