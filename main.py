from scipy import optimize
import numpy as np

# --- Function 1 ---
def easy_f(x):
    return (x ** 2) - 2
def easy_f_prime(x):
    return 2 * x

# --- Function 2 ---
def med_f(x):
    return np.sin(x) - (0.5 * x)
def med_f_prime(x):
    return np.cos(x) - 0.5

# --- Function 3 ---
def hard_f(x):
    return x * np.exp(-x) - 0.1
def hard_f_prime(x):
    return np.exp(-x) - x * np.exp(-x)


def run_methods(name, f, fprime, x0, a, b):
    print(f"\n=== {name} ===")

    # brute-force
    brute_res = optimize.brute(f, ((a, b),), full_output=True, finish=None)
    print("Brute root:", brute_res[0], ", Residual:", abs(f(brute_res[0])))

    # bisect
    root, info = optimize.bisect(f, a, b, full_output=True)
    print("Bisect root:", root, ", Iterations:", info.iterations, ", Residual:", abs(f(root)))

    # newton
    root, info = optimize.newton(f, x0, fprime=fprime, full_output=True)
    print("Newton root:", root, ", Iterations:", info.iterations, ", Residual:", abs(f(root)))

    # secant
    root, info = optimize.newton(f, x0, full_output=True)
    print("Secant root:", root, ", Iterations:", info.iterations, ", Residual:", abs(f(root)))

    # brentq
    root, info = optimize.brentq(f, a, b, full_output=True)
    print("Brent root:", root, ", Iterations:", info.iterations, ", Residual:", abs(f(root)))


# Запуск для трёх функций
run_methods("Easy function", easy_f, easy_f_prime, x0=2, a=0, b=3)
run_methods("Medium function", med_f, med_f_prime, x0=2, a=1, b=3)
run_methods("Hard function", hard_f, hard_f_prime, x0=2, a=1, b=5)

# --- System of equations example ---
def system(vars):
    x, y = vars
    return [x**2 + y**2 - 4,  # circle
            x - y]            # line

print("\n=== System of equations (fsolve) ===")
sol1 = optimize.fsolve(system, [1, 1])   # начальное приближение (положительное решение)
sol2 = optimize.fsolve(system, [-1, -1]) # начальное приближение (отрицательное решение)

print("Solution 1:", sol1, ", Residuals:", system(sol1))
print("Solution 2:", sol2, ", Residuals:", system(sol2))