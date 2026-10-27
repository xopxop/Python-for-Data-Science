from PIL import Image
import numpy as np
from load_image import ft_load


def grayOutImg(imageNp) -> np.ndarray:
    grayscaleRGB = [0.2989, 0.5870, 0.1140]

    return np.dot(imageNp[..., :3], grayscaleRGB)


def centerImg(imgNp):
    h, w = imgNp.shape[:2]
    newH, newW = 400, 400
    startH, startW = (h - newH) // 2, (w - newW) // 2
    croppedImgNp = imgNp[startH: startH + newH, startW: startW + newW]
    return croppedImgNp


def showImg(slicedImageArray):
    zoomedImage = Image.fromarray(slicedImageArray)
    zoomedImage.show()
    return 0


def main():
    imgNp = ft_load("animal.jpeg")
    print(imgNp)
    croppedImgNp = centerImg(imgNp)
    print(f"New shape after slicing: {croppedImgNp.shape}")
    print(croppedImgNp)
    changedColorImgNp = grayOutImg(croppedImgNp)
    showImg(changedColorImgNp)
    return 0


if __name__ == "__main__":
    main()
