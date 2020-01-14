import sys

try:
    a=1/0
    print(a)
except:
    print(sys.exc_info())


try:
    a=1/0
    print(a)
except(ZeroDivisionError):
    # print(sys.exc_info())
    print("handled exception")
print("hi")


# raising an exception
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))






