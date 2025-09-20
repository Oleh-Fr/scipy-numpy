from scipy import optimize, stats
import matplotlib.pyplot as plt
import numpy as np

def easy_f(x):
    return (x ** 2) - 2

def med_f(x):
    return np.sin(x) - (0.5 * x)

def hard_f(x):
    return x * np.exp(-x) - 0.1

#brute-force
ez_brute = optimize.brute(easy_f, ((1,10),)) # [-8.8817842e-16]
m_brute = optimize.brute(med_f, ((1,10),)) # [11.51916504]
h_brute = optimize.brute(hard_f, ((1,10),)) # [57.5]


