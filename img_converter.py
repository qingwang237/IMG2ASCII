"""The image to ASCII converting functions library.

Contains img2ascii() which does the converting jobs

"""

from PIL import Image
import numpy as np

# predifend size that any large images will be resized to
SIZE = (64, 64)
# the characters used to simulate the greyscale levels
# from the lightest to the darkest
CHAR_GRADIENT_SIMULATOR = ' .,:;irsXA253hMHGS#9B&@'


def img2ascii(imagefile, scale_factor=1.0, gradient_corrF=1.5,
              width_corrF=7 / 4):
    """Convert an image filestorage object to its ASCII form.

    scale_factor: scaling factor during ASCII converstion, default to 1.
    gradient_corrF: correcting factor for image gradient, default to 1.5.
    width_corrF: correcting factor for fonts width and height, default to 7/4.
    """
    # open image and convert to greyscale
    image = Image.open(imagefile).convert('LA')
    # slim down the image
    image.thumbnail(SIZE, Image.ANTIALIAS)
    # create a numpy array using the predifend characters for different levels
    chars = np.asarray(list(CHAR_GRADIENT_SIMULATOR))
    # resize the image and correct the width dimension if necessary
    new_size = (round(image.size[0] * scale_factor * width_corrF),
                round(image.size[1] * scale_factor))
    # Get overall intensity for each pixel in the image
    img = np.sum(np.asarray(image.resize(new_size)), axis=2)
    # normalized to its minimum and maxium intensity and convert each pixel to
    # the corresponding characters
    img -= img.min()
    img = (1.0 - img / img.max())**gradient_corrF * (chars.size - 1)
    # generate printable results
    printable_img = "\n".join(("".join(r) for r in chars[img.astype(int)]))
    # print(printable_img)
    return printable_img.split('\n')
