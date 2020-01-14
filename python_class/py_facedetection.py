import cv2

# load image
img1 = cv2.imread('new.jpg', 1)
img=cv2.resize(img1,(500,500))

# Convert into GRAYSCALE
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load a trained classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1,
                                      minNeighbors=5, minSize=(30, 30))

# Draw a bounding rectangle around faces
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display output
cv2.imshow('color image', img)

# Press any key to terminate
cv2.waitKey(0)

# Destroys all the windows we created to free up memory
# cv2.destroyAllWindows()
