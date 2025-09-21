import numpy as np
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


def run_methods_and_collect_results(name, f, fprime, x0, a, b):
    """
    Runs various root-finding methods on a function and collects the results.
    """
    results = []

    # brute-force
    try:
        brute_res = optimize.brute(f, ((a, b),), full_output=True, finish=None)
        brute_root = brute_res[0]
        results.append(["Brute-force", "Да", "N/A", f"{abs(f(brute_root)):.2e}", "Нет", "Низкая"])
    except Exception:
        results.append(["Brute-force", "Нет", "N/A", "N/A", "Нет", "Низкая"])

    # bisect
    try:
        bisect_root, info = optimize.bisect(f, a, b, full_output=True)
        results.append(["Bisect", "Да", info.iterations, f"{abs(f(bisect_root)):.2e}", "Нет", "Низкая"])
    except Exception:
        results.append(["Bisect", "Нет", "N/A", "N/A", "Нет", "Низкая"])

    # newton
    try:
        newton_root, info = optimize.newton(f, x0, fprime=fprime, full_output=True)
        results.append(["Newton", "Да", info.iterations, f"{abs(f(newton_root)):.2e}", "Да", "Высокая"])
    except Exception:
        results.append(["Newton", "Нет", "N/A", "N/A", "Да", "Высокая"])

    # secant
    try:
        secant_root, info = optimize.newton(f, x0, full_output=True)
        results.append(["Secant", "Да", info.iterations, f"{abs(f(secant_root)):.2e}", "Нет", "Высокая"])
    except Exception:
        results.append(["Secant", "Нет", "N/A", "N/A", "Нет", "Высокая"])

    # brentq
    try:
        brentq_root, info = optimize.brentq(f, a, b, full_output=True)
        results.append(["Brentq", "Да", info.iterations, f"{abs(f(brentq_root)):.2e}", "Нет", "Низкая"])
    except Exception:
        results.append(["Brentq", "Нет", "N/A", "N/A", "Нет", "Низкая"])

    return results


if __name__ == '__main__':
    # Сбор результатов для каждой функции
    all_results = {}
    all_results["Easy Function: f(x) = x^2 - 2"] = run_methods_and_collect_results("easy_f", easy_f, easy_f_prime, 2, 1,
                                                                                   3)
    all_results["Medium Function: f(x) = sin(x) - 0.5x"] = run_methods_and_collect_results("med_f", med_f, med_f_prime,
                                                                                           2, 1, 3)
    all_results["Hard Function: f(x) = xe^(-x) - 0.1"] = run_methods_and_collect_results("hard_f", hard_f, hard_f_prime,
                                                                                         0.1, 0, 1)

    # Имя выходного CSV-файла
    filename = "comparison_results.csv"

    # Заголовки для CSV
    headers = ["Метод", "Сходимость", "Кол-во итераций", "Точность", "Требование производной", "Чувствительность"]

    # Запись данных в CSV-файл
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            for func_name, rows in all_results.items():
                writer.writerow([func_name])
                writer.writerow(headers)
                writer.writerows(rows)
                writer.writerow([])

        print(f"Файл '{filename}' успешно создан.")

    except Exception as e:
        print(f"Произошла ошибка при создании файла: {e}")

    # Plotting part is removed as the focus is on CSV generation
