x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y) #rounds down from 2.8 to 2

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#generating random numbers
import random
print(random.randrange(1, 10))



#specifying variable types
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2