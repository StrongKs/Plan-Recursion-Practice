# 1, 1, 2, 3, 5, 8, 13, 21...

def fib(self, place):
    if place == 1:
        return place
    
x = 1
y = 1

# 1
print(1, 1)

#2
print(1, 1)

#3
x = x+y
print(x, 2)

#4
y = x+y
print(y, 3)

#5
x = x+y
print(x, 5)

#6
y = x+y
print(y, 8)
