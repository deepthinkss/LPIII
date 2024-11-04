def printFibonacci(n, a=0, b=1):
    if n > 0:
        n3 = a + b
        print(n3, end=" ")
        printFibonacci(n - 1, b, n3)

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    print("Fibonacci Series: ", end="")
    print("0 1 ", end="")
    printFibonacci(n - 2)  # n-2 because 2 numbers are already printed
