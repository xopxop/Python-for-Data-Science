from PIL import Image
import numpy as np

MAX_BRIGHTNESS = 255


def showImg(array):
    img = Image.fromarray(array)
    img.show()


def ft_invert(array) -> np.ndarray:
    invert = np.zeros(array.shape, dtype=array.dtype)

    for r in range(len(array)):
        for c in range(len(array[r])):
            invert[r][c][0] = MAX_BRIGHTNESS - array[r][c][0]
            invert[r][c][1] = MAX_BRIGHTNESS - array[r][c][1]
            invert[r][c][2] = MAX_BRIGHTNESS - array[r][c][2]
    showImg(invert)
    return invert


def ft_red(array) -> np.ndarray:
    redFilter = np.zeros(array.shape, dtype=array.dtype)

    for r in range(len(array)):
        for c in range(len(array[r])):
            redFilter[r][c][0] = array[r][c][0]
    showImg(redFilter)
    return redFilter


def ft_green(array) -> np.ndarray:
    greenFilter = np.zeros(array.shape, dtype=array.dtype)

    for r in range(len(array)):
        for c in range(len(array[r])):
            greenFilter[r][c][1] = array[r][c][1]
    showImg(greenFilter)
    return greenFilter


def ft_blue(array) -> np.ndarray:
    blueFilter = np.zeros(array.shape, dtype=array.dtype)

    for r in range(len(array)):
        for c in range(len(array[r])):
            blueFilter[r][c][2] = array[r][c][2]
    showImg(blueFilter)
    return blueFilter


def ft_grey(array) -> np.ndarray:
    greyFilter = np.zeros(array.shape, dtype=array.dtype)

    for r in range(len(array)):
        for c in range(len(array[r])):
            red = array[r][c][0]
            green = array[r][c][1]
            blue = array[r][c][2]
            value = (red * 0.2989) + (green * 0.5870) + (blue * 0.1140)
            greyFilter[r][c][0] = value
            greyFilter[r][c][1] = value
            greyFilter[r][c][2] = value
    showImg(greyFilter)
    return greyFilter
