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

# bisect
ez_bisect = optimize.bisect(easy_f, 1, 10) #1.4142135623732202
m_bisect = optimize.bisect(med_f, 1, 10) #1.895494267033314
h_bisect = optimize.bisect(hard_f, 1, 10) #3.577152063957442

# newton method
ez_newton = optimize.newton(easy_f, 2) #1.4142135623730954
m_newton = optimize.newton(med_f, 2) #1.895494267033981
h_newton = optimize.newton(hard_f, 2) #3.577152063957297

