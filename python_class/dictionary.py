# Creating an empty Dictionary
#
Dict = {}
print("Empty Dictionary: ")
print(Dict)
#
#Creating a Dictionary  with Integer Keys
Dict = {1: 'python', 2: 'programming', 3: 'language'}
print("\nDictionary with the use of Integer Keys: ")

print(Dict)
Dict = {'Name': 'python', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary with dict() method
Dict = dict({1: 'python', 2: 'program', 3: 'language'})
print("\nDictionary with the use of dict(): ")
print(Dict)
# #
# # Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'python'), (2, 'program')])
print("\nDictionary with each item as a pair: ")
print(Dict)
#
# # Creating a Nested Dictionary as shown in the below image
Dict = {1: 'python', 2: 'program',3: {'A': 'Welcome', 'B': 'To', 'C': 'internship'}}
print(Dict)
#
# CREATE DICTIONARY
mydict = {'StuName': 'Ajeet', 'StuAge': 30, 'StuCity': 'Agra'}
print("Student Age is:", mydict['StuAge'])
print("Student City is:", mydict['StuCity'])
# #
# # CHANGE OF VALUES
mydict['StuAge'] = 31
mydict['StuCity'] = 'Noida'
#Creating a Dictionary with Mixed keys
print("Student Age after update is:", mydict['StuAge'])
print("Student City after update is:", mydict['StuCity'])

# # ADDING NEW ENTRY
mydict['StuClass'] = 'Jr.KG'
print("Student Name is:", mydict['StuName'])
print("Student Class is:", mydict['StuClass'])
print(mydict)
#
# # loop
for e in mydict:
   print("Key:",e,"Value:",mydict[e])
#
for x in mydict:
     print(x)
#
for x in mydict:
   print(mydict[x])
#
for x in mydict.values():
   print(x)
#
for x, y in mydict.items():
   print(x, y)
#
#
# # accesing a element from a Dictionary
#
# # Creating a Dictionary
Dict = {1: 'language', 'name': 'python', 3: 'program'}
#
# # accessing a element using key
print("Acessing a element using key:")
print(Dict['name'])
#
# # accessing a element using key
print("Acessing a element using key:")
print(Dict[1])
#
# # accessing a element using get()
# # method
print("Acessing a element using get:")
print(Dict.get(2))

# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# # Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)
# #
# # # Deleting a Key from
# # # Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
# #
# # Deleting a Key
# using pop()
#Dict.pop(2)
print("\nPopping specific element: ")
print(Dict)
#
# Deleting a Key
#using popitem()
Dict.popitem()
print("\nPops first element: ")
print(Dict)
#
# # Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)