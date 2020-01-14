#creating a file
file = open('demo.txt', 'w')
file.write('Hello World \n')
file.write('This is our new text file')
file.write('and this is another line.')
file.write('Why? Because we can do it this easily.')
file.close()

##read operation
f = open('demo.txt','r')
print(f.read())
#
# ##read by no.of letters operation
f = open('demo.txt','r')
print(f.read(10))
#
# ##read line by line
f = open('demo.txt','r')
print(f.readline())
print(f.readlines())
#
# # #looping
file = open('demo.txt', 'r')
for line in file:
    print(line)
#
#
file.close()
#
with open("demo.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)