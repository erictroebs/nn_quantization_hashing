import sys

import imageio
import numpy as np
from skimage.color import rgb2gray, rgba2rgb
from skimage.transform import resize


def hash(path):
    # load image
    print("loading image", path)
    image = imageio.imread(path)

    # handle png images with alpha channel
    if len(image.shape) > 2 and image.shape[2] == 4:
        print("removing alpha channel")
        image = rgba2rgb(image)

    # rescaling
    print("rescaling image")
    image = resize(image, (8, 8))

    # convert to grayscale
    if len(image.shape) > 2 and image.shape[2] == 3:
        print("converting to grayscale")
        image = rgb2gray(image)

    # calculate mean
    print("calculating mean", end="")

    mean = 0
    for y, x in np.ndindex(image.shape[:2]):
        mean += image[y, x]

    mean = mean / (8 * 8)

    print(" = ", mean)

    # apply threshold
    print("applying threshold")

    for y, x in np.ndindex(image.shape[:2]):
        if image[y, x] < mean:
            image[y, x] = 0
        else:
            image[y, x] = 1

    # calculate hash
    print("calculating hash", end="")

    hash_value = 0
    for y, x in np.ndindex(image.shape[:2]):
        hash_value <<= 1
        hash_value += int(image[y, x])

    print(" =", '%#x' % hash_value)
    print()

    return hash_value


def hamming(a, b):
    distance = 0

    while a > 0 or b > 0:
        if (a & 1) != (b & 1):
            distance += 1

        a >>= 1
        b >>= 1

    return distance


if __name__ == '__main__':
    hashes = [hash(path) for path in sys.argv[1:]]
    print()

    for i1, p1 in enumerate(sys.argv[1:]):
        for i2, p2 in enumerate(sys.argv[1:]):
            print(p1, "vs", p2)
            print(hamming(hashes[i1], hashes[i2]))
            print()
