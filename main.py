import scipy.special as scp
import matplotlib.pyplot as plt
import numpy as np

def easy_f(x):
    return (x ** 2) - 2

def med_f(x):
    return np.sin(x) - (0.5 * x)

def hard_f(x):
    return x * np.exp(-x) - 0.1