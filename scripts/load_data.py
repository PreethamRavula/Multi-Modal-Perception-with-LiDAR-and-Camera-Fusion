import cv2
import matplotlib.pyplot as plt 

# Loading an image
img = cv2.imread('../data/training/image_2/000000.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the image
plt.imshow(img)
plt.title("Camera Image")
plt.axis("off")
plt.show()
