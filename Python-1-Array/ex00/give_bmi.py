import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    heightArray = np.array(height)
    weightArray = np.array(weight)

    return (weightArray / (heightArray**2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmiArray = np.array(bmi)

    return (bmiArray > limit).tolist()
