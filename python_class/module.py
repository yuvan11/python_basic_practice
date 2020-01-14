from math import sqrt, factorial
import math

print(sqrt(16))
print(factorial(6))
print(math.pi)
print(math.degrees(2))
print(math.radians(60))
print(math.sin(2))
print(math.cos(0.5))
print(math.tan(0.23))

# #
import random

print(random.randint(0, 5))
print(random.random())
print(random.random() * 100)
List = [1, 4, True, 800, "python", 27, "hello"]
print(random.choice(List))

import platform

x = platform.system()
print(x)


import mymodule

mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)