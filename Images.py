#Name: Justin K Too
#Email: justin.too27@myhunter.cuny.edu
#This program changes the color if the img

import matplotlib.pyplot as plt
import numpy as np

userInput = input("Enter name of img file: ")
userOutput = input("Enter output file name: ")
img = plt.imread(userInput)
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:, :, 0] = 0
img2[:, :, 1] = 0

plt.imshow(img2)
plt.show()
plt.imsave(userOutput, img2)
