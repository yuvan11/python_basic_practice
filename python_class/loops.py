count = 0
while (count < 3):
    count = count + 1
    print("Hello welcome")
#
#
#
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")
#
print("List Iteration")
l = ["apple", "orange", "banana"]
for i in l:
    print(i)
print("\nTuple Iteration")
t = ("grapes", "kiwi", "pearls")
for i in t:
    print(i)
s = "python"
for i in s:
    print(i)

# Iterating over dictionary
# print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
print(d)
for i in d:
    print(i, d[i])

# Iterating by index

list = ["python", "program", "language"]
for index in range(len(list)):
    print(list[index])
#
# list = ["system", "code", "platform"]
for index in range(len(list)):
     print(list[index])
else:
    print("Inside Else Block")
#
# # nested for loops in Python
for i in range(1, 5):
     for j in range(i):
         print(i, end=' ')
         print()

# Prints all letters except 'e' and 's'
for letter in 'python language':
    if letter == 'l':
          continue
    print('Current Letter :', letter)
#
list=["A","B","C"]
for v in list:
     print(v)
#
for v in list(list):
    print(v)

a=10
for v in range(a):
     print(v)