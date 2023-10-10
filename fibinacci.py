def fib(num1, num2, index):
    if index == 0:
        return num1
    
    if index % 2 == 0: # if even
        return fib(num1+num2, num2, index-1)
    else:
        return fib(num1, num1+num2, index-1)


index = int(input("What index of fibiunacci do you want?    "))

res = fib(1, 1, index-1)

print(
    res
)

[1,1,2,3,5,8,]