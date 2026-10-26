import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    familyArray = np.array(family)
    slicedFamilyArray = familyArray[start:end]

    print(f"My shape is : {familyArray.shape}")
    print(f"My new shape is : {slicedFamilyArray.shape}")
    return slicedFamilyArray.tolist()
