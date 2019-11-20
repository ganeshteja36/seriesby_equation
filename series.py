def series(n):
    if n <=1:
        return n

    else:
        return ((2)*(n-1)) + ((2)*(n-2))


nterms = int(input("Enter the terms? "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(series(i))
