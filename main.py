import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import csv


# --- Define the functions and their derivatives ---
def easy_f(x):
    return (x ** 2) - 2


def easy_f_prime(x):
    return 2 * x


def med_f(x):
    return np.sin(x) - (0.5 * x)


def med_f_prime(x):
    return np.cos(x) - 0.5


def hard_f(x):
    return x * np.exp(-x) - 0.1


def hard_f_prime(x):
    return np.exp(-x) - x * np.exp(-x)


def run_methods(name, f, fprime, x0, a, b, ax):
    """
    Runs various root-finding methods on a function and plots the results.

    Args:
        name (str): The name of the function being tested.
        f (callable): The function to find the root of.
        fprime (callable): The derivative of the function.
        x0 (float): The initial guess for Newton's and Secant methods.
        a (float): The lower bound of the interval for bracketing methods.
        b (float): The upper bound of the interval for bracketing methods.
        ax (matplotlib.axes.Axes): The axes object to plot on.
    """
    print(f"\n=== {name} ===")

    # search area
    ax.axvspan(a, b, facecolor='gray', alpha=0.2, label='Область пошуку')

    # brute-force
    brute_res = optimize.brute(f, ((a, b),), full_output=True, finish=None)
    brute_root = brute_res[0]
    print("Brute root:", brute_root, ", Residual:", abs(f(brute_root)))
    ax.scatter(brute_root, f(brute_root), label=f"Brute-force Root ({name})", color='purple', marker='o', s=100)

    # bisect
    bisect_root, info = optimize.bisect(f, a, b, full_output=True)
    print("Bisect root:", bisect_root, ", Iterations:", info.iterations, ", Residual:", abs(f(bisect_root)))
    ax.scatter(bisect_root, f(bisect_root), label=f"Bisect Root ({name})", color='red', marker='o', s=100)

    # newton
    newton_root, info = optimize.newton(f, x0, fprime=fprime, full_output=True)
    print("Newton root:", newton_root, ", Iterations:", info.iterations, ", Residual:", abs(f(newton_root)))
    ax.scatter(newton_root, f(newton_root), label=f"Newton Root ({name})", color='green', marker='o', s=100)

    # secant
    secant_root, info = optimize.newton(f, x0, full_output=True)
    print("Secant root:", secant_root, ", Iterations:", info.iterations, ", Residual:", abs(f(secant_root)))
    ax.scatter(secant_root, f(secant_root), label=f"Secant Root ({name})", color='blue', marker='o', s=100)

    # brentq
    brentq_root, info = optimize.brentq(f, a, b, full_output=True)
    print("Brentq root:", brentq_root, ", Iterations:", info.iterations, ", Residual:", abs(f(brentq_root)))
    ax.scatter(brentq_root, f(brentq_root), label=f"Brentq Root ({name})", color='black', marker='o', s=100)


# --- Plotting the functions ---
if __name__ == '__main__':
    # Plotting easy_f and saving separately
    fig_easy, ax_easy = plt.subplots(figsize=(10, 6))
    x_easy = np.linspace(-5, 5, 1000)
    ax_easy.plot(x_easy, easy_f(x_easy), label=r'$f(x) = x^2 - 2$')
    ax_easy.set_title("Easy Function: $x^2 - 2$")
    ax_easy.grid(True)
    ax_easy.axhline(0, color='black', linewidth=0.8)
    run_methods("easy_f", easy_f, easy_f_prime, 2, 1, 3, ax_easy)
    ax_easy.legend()
    fig_easy.savefig("./plots/easy_f.png")
    plt.close(fig_easy)

    # Plotting med_f and saving separately
    fig_med, ax_med = plt.subplots(figsize=(10, 6))
    x_med = np.linspace(-1, 3, 1000)
    ax_med.plot(x_med, med_f(x_med), label=r'$f(x) = \sin(x) - 0.5x$')
    ax_med.set_title("Medium Function: $\sin(x) - 0.5x$")
    ax_med.grid(True)
    ax_med.axhline(0, color='black', linewidth=0.8)
    run_methods("med_f", med_f, med_f_prime, 2, 1, 3, ax_med)
    ax_med.legend()
    fig_med.savefig("./plots/med_f.png")
    plt.close(fig_med)

    # Plotting hard_f and saving separately
    fig_hard, ax_hard = plt.subplots(figsize=(10, 6))
    x_hard = np.linspace(-1, 5, 1000)
    ax_hard.plot(x_hard, hard_f(x_hard), label=r'$f(x) = xe^{-x} - 0.1$')
    ax_hard.set_title("Hard Function: $xe^{-x} - 0.1$")
    ax_hard.grid(True)
    ax_hard.axhline(0, color='black', linewidth=0.8)
    run_methods("hard_f", hard_f, hard_f_prime, 0.1, 0, 1, ax_hard)
    ax_hard.legend()
    fig_hard.savefig("./plots/hard_f.png")
    plt.close(fig_hard)

    plt.show()
