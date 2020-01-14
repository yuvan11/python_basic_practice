# # creating Set
myset = {"hi", 2, "bye", "Hello World"}
print(myset)
# checking
print(2 in myset)

print("hi" in myset)

print("welcome" in myset)

# looping
for a in myset:
    print(a)

# adding an item
myset.add(99)
print("Set after adding 99:", myset)

myset.update(["orange", "mango", "grapes"])
print(myset)

# removing an item
myset.remove("bye")
print("Set after removing bye:", myset)

myset.discard("grapes")
print(myset)

x = myset.pop()
print(x)
print(myset.pop())

myset.clear()
print(myset)
#

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#
# # deleting
del thisset
print(thisset)