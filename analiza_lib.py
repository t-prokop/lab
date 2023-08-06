import numpy as np
import matplotlib.pyplot as plt
import traceback
from numpy.typing import ArrayLike
from scipy.optimize import curve_fit


def sigma_test(val1: float, val2: float, sigma1, sigma2) -> bool:
    try:
        if sigma1 < 0 or sigma2 < 0:
            raise ValueError("Sigma musza byc >= 0")
        if sigma1 == 0 and sigma2 == 0:
            raise ValueError("Chociaz jedno sigma musi byc niezerowe")
        if (val2-val1) < 3*np.sqrt(sigma1**2 + sigma2**2):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        print(traceback.print_exc(e))


def get_value_from_res(results: ArrayLike, is_population=False) -> tuple[float, float]:
    arr = np.array(results, dtype=np.float64)
    avg = np.mean(arr)
    if is_population:
        sigma = np.std(arr)*(len(arr)-1)/len(arr)
    else:
        sigma = np.std(arr)
    return avg, sigma


def fit_function():
    pass
