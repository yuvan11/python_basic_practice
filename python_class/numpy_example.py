import numpy as np

a=np.array([1,2,3])
print(a)
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)


b=np.array([(1,2,3,4),(4,5,6,7)])
print(b)
print(b.ndim)
print(b.shape)
print(b.reshape(4,2))
print(b)
print(b[0,2])
print(b[1,3])


#linespace
a=np.linspace(1,5,10)
print(a)

#min,max,sum
print(b.min())
print(b.max())
print(b.sum())

# axis
print(b.sum(axis=0))      #columns
print(b.sum(axis=1))       #rows

print(np.sqrt(b))
print(np.std(b))

c=np.array([(4,3,2,1),(7,6,5,4)])

print(b+c)
print(b-c)
print(b*c)
print(b/c)
# # # concatenATE

print(np.vstack((b,c)))
print(np.hstack((b,c)))
# #
print(c.ravel())
#
# Create an array of ones
print(np.ones((3,4)))
# #
# # Create an array of zeros
print(np.zeros((2,3,4),dtype=np.int16))
# #
# # Create an array with random values
print(np.random.random((2,2)))
#
# # Create an empty array
print(np.empty((3,2)))
# #
# # Create a full array
print(np.full((2,2),7))
# #
# # # Create an array of evenly-spaced values
print(np.arange(10,25,5))
# #
# # Create an array of evenly-spaced values
print(np.linspace(0,2,9))
print(np.eye(2))


print(np.identity(5))