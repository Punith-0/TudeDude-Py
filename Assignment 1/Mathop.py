def main() :
    num1 = float(input("Enter the first number :"))
    num2 = float(input("Enter the second number :"))

    print(f"Addition :{num1 + num2 }")
    print(f"Subraction :{num1 - num2 }")
    print(f"Multiplication :{num1 * num2 }")
    print(f"Division :{num1 / num2 }" if num2 != 0 else "Division : 0")

if __name__ == "__main__" :
    main()