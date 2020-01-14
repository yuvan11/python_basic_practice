def my_function():
    print("Hello From My Function!")
my_function()


#  Define a function `plus()`
def plus(a, b):
    print(a + b)
plus(2,3)

# Create a `Summation` class
class Summation:
    def sum(self,a, b):
        contents = a + b
        print(contents)
        return contents

sumInstance = Summation()
sumInstance.sum(1,2)


 # Define `plus()`
def plus(a,b):
  sum = a + b
  print(sum)
  return (sum, a)
  #print(sum)
#two ways of calling fn plus
# one way
plus(2,3)

# another way
v1,v2= plus(3,4)

print(v1)


# # Define `plus()` function
def plus(a, b=2):
    return a + b

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  return sum(args)

# Calculate the   sum
a=plus(1,4,5)
print(a)
