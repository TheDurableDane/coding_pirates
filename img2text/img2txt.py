"""
Image to text file conversion

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 29jan2017
"""

import matplotlib.pylab as plt

# Read and plot image
img = plt.imread('cameraman.png')
img = img[:, :, 0]*255
plt.imshow(img, cmap='gray')

# Convert image to text
img_text = ''
for row in img:
    for pixel in row:
        if pixel > 255*3/4:
            img_text += ' '
        elif pixel <= 255*3/4 and pixel > 255*2/4:
            img_text += '.'
        elif pixel <= 255*2/4 and pixel > 255*1/4:
            img_text += '!'
        else:
            img_text += '#'

    img_text += '\n'

# Write text to file
with open("cameraman.txt", "w") as text_file:
    text_file.write("{}".format(img_text))
