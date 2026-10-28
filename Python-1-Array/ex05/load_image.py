from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        im = Image.open(path)
        imageArray = np.array(im)
        print(f"The shape of image is {imageArray.shape}")
        return imageArray
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
