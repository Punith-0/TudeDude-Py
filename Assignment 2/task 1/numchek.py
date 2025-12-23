def numchek() :
    num : int = int(input("Enter the number : ")) 

    print(f"{num} is Even" if num % 2 == 0 else f"{num} is odd")
 
'''def numchek() :
    num : int = int(input("Enter the number : ")) 

    print(f"{num} is Even" if num & 1  == 0 else f"{num} is odd")'''

if __name__ == "__main__" :
    numchek()
