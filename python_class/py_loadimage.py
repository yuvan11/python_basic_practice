"""
type these in terminal to install packages
pip install opencv-python
pip install numpy,matplotlib,scipy
"""
import cv2
# load a color(RGB) image
img = cv2.imread('new.jpg', 1)
resize1=cv2.resize(img,(500,500))

# convert image into GRAYSCALE image
grayimg = cv2.imread('new.jpg', 0)
resize2=cv2.resize(grayimg,(500,500))
# display image dimension
print(resize1,resize2)
# display image
# cv2.imshow('color image', resize1)
# cv2.imshow('gray image', resize2)

# Press any key to terminate
cv2.waitKey(0)

# Destroys all the windows we created to free up memory
cv2.destroyAllWindows()
