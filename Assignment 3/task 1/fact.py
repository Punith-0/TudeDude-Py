def fact(num : int):
    if num == 0 or num == 1 :
        return 1 
    return num* fact(num -1)
def main() :
    num : int = int(input("Enter a number : "))
    print(f"The factorial of {num} is {fact(num)}")

main()