number = int(input("How many numbers you want? "))
n1 = 0
n2 = 1
count = 0
if number <=0:
    print("Enter any positive number")
elif  number ==1:
    print("Fibonacci series:")
    print(n1)
else:
    print("Fibonacci sequence:")

    while count < number:
        print(n1)
        nth = n1 + n2

        #update the values

        n1 = n2
        n2 = nth
        count +=1
