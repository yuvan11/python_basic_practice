# empty tuple
my_tuple = ()
print(my_tuple)

# create tuple
tup = ('python', 'program','language')
print(tup)

# tuple unpacking is also possible

a,b,c= tup
print(a)
print(b)
print(c)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
#
# only parentheses is not enough
my_tuple = ("hello")
print(type(my_tuple))

# need a comma at the end
my_tuple = ("hello",)
print(type(my_tuple))


# Code for concatenating 2 tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'program')

print(tuple1 + tuple2)

# Code for creating nested tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'program')
tuple3 = (tuple1, tuple2)
print(tuple3)

# Code to create a tuple with repetition

tuple3 = ('python',) * 3
print(tuple3)

# code to test slicing

tuple1 = (0, 1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# Code for printing the length of a tuple

tuple2 = ('python', 'program')
print(len(tuple2))

# Code for converting a list and a string into a tuple

list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python'))  # string 'python'


# indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])

print(my_tuple[5])

print(my_tuple[-1])

print(my_tuple[-6])

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])

print(n_tuple[1][1])

my_tuple = ('a','p','p','l','e',)

# Count
print(my_tuple.count('p'))

# Index
print(my_tuple.index('l'))

# methods
my_tuple = ('a','p','p','l','e',)

# In operation
print('a' in my_tuple)

print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)

# example
txt = 'but soft what light in yonder window breaks'
words = txt.split()
print(words)
t = list()
for word in words:
    t.append((len(word), word))
print(t)

t.sort(reverse=True)
print(t)

res = list()
res1=list()
for length,word in t:
    res.append(word)
    res1.append(length)
    # print(length)

print(res)
print(res1)

# Code for deleting a tuple

# tuple3 = (0, 1)
# del tuple3
# print(tuple3)

# code to test that tuples are immutable

# tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4
# print(tuple1)



tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

#Packing and Unpacking
x = ("-", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)

#Comparing tuples
#case 1
a=(5,6)
b=(5,7)
if (a>b):
    print("a is bigger")
else:
    print("b is bigger")



#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.keys()
print(b)

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print(x[2:4])