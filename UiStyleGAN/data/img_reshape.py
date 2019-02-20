# This code is used to reshape images into 256 * 256 dimensions.

import os, re
from scipy import ndimage, misc

for root, dirnames, filenames in os.walk("C:/Users/Sid/Share/PIX2CODE"):
    for idx, filename in enumerate(filenames):
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            filepath = os.path.join(root, filename)
            print(filename)
            image = ndimage.imread(filepath, mode="RGB")
            image_resized = misc.imresize(image, (256, 256))
            misc.imsave(str(idx) + '.png', image_resized)