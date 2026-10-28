from PIL import Image
import numpy as np
from load_image import ft_load


def grayOutImg(imageNp) -> np.ndarray:
    grayscaleRGB = [0.2989, 0.5870, 0.1140]

    return np.dot(imageNp[..., :3], grayscaleRGB)


def cropImg(imgNp):
    h, w = imgNp.shape[:2]
    newH, newW = 400, 400
    startH, startW = (h - newH) // 2, (w - newW) // 2
    croppedImgNp = imgNp[startH: startH + newH, startW: startW + newW]
    return croppedImgNp


def showImg(imgNp):
    zoomedImage = Image.fromarray(imgNp)
    zoomedImage.show()
    return 0


def transpose(imgNp):
    transposeImgNp = np.zeros((imgNp.shape[1], imgNp.shape[0], imgNp.shape[2]))

    for r in range(len(imgNp)):
        for c in range(len(imgNp[r])):
            for rgb in range(len(imgNp[r][c])):
                transposeImgNp[c][r][rgb] = imgNp[r][c][rgb]
    return imgNp


def main():
    imgNp = ft_load("animal.jpeg")
    print(imgNp)
    croppedImgNp = cropImg(imgNp)
    transposedImgNp = transpose(croppedImgNp)
    print(f"New shape after Transpose: {transposedImgNp.shape}")
    print(transposedImgNp)
    changedColorImgNp = grayOutImg(transposedImgNp)
    showImg(changedColorImgNp)
    return 0


if __name__ == "__main__":
    main()
