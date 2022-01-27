import math
def x(x, y):
    return ((math.pi - x) ** 2 + (math.e - y)**2) < 2

print(x(3, 4))
print(x(4, 4))
print(x(2, 4))
print(x(2, 2))
print(x(3, 2))
print(x(4, 2))

print(math.sqrt((1 - math.sqrt(19)) ** 2 + (1 - math.sqrt(19)) ** 2 + (1 - math.sqrt(19)) ** 2))
