````markdown
# Root-Finding Methods Comparison

This repository contains a Python project that compares several numerical methods for finding the roots of functions. The project uses the `NumPy`, `SciPy`, and `Matplotlib` libraries to perform calculations, analyze convergence, and visualize the results.

The code provides a practical example of how different algorithms—such as the Bisection Method, Newton's Method, and Brent's Method—perform on various functions with different levels of complexity.

## Key Features

* **Algorithmic Comparison**: Evaluates the performance of five popular root-finding methods:
    * Brute-force
    * Bisection Method
    * Newton's Method (with and without explicit derivative)
    * Brent's Method (`brentq`)
* **Visualization**: Generates and saves plots showing the functions and the roots found by each method, along with their search intervals.
* **Data Export**: Creates a CSV file summarizing the performance of each method based on convergence, number of iterations, and accuracy.

## Project Structure

* `plot_functions.py`: The main script that performs the root-finding calculations and generates the plots.
* `generate_csv.py`: A utility script that runs the analysis and exports the results to a CSV file.
* `plots/`: A directory where the generated plot images are saved.
* `comparison_results.csv`: The output CSV file with the analysis results.

## Methods Compared

### 1. Brute-force

A simple, non-iterative method that scans a given interval for a root. It is not very precise but can be useful for a rough estimate.

### 2. Bisection Method

A robust, guaranteed-to-converge method that repeatedly halves a search interval until a root is found. It is slow but very reliable.

### 3. Newton's Method

A fast, iterative method that uses the function's derivative to quickly converge on a root. It is very efficient but can fail if the initial guess is not close enough to the root.

### 4. Secant Method

A variation of Newton's Method that approximates the derivative using a secant line. It doesn't require an explicit derivative, making it more flexible, though slightly slower than the classic Newton's Method.

### 5. Brent's Method (`brentq`)

A hybrid method that combines the speed of the secant method with the guaranteed convergence of the bisection method. It is often the preferred method for general-purpose root-finding.

## Getting Started

### Prerequisites

You need Python 3 and the following libraries installed:
* `numpy`
* `scipy`
* `matplotlib`

You can install them using `pip`:
```bash
pip install numpy scipy matplotlib
````

### Running the Code

1.  Clone this repository:
    ```bash
    git clone [https://github.com/Oleh-Fr/scipy-numpy.git](https://github.com/Oleh-Fr/scipy-numpy.git)
    cd scipy-numpy
    ```
2.  Run the main script to generate plots:
    ```bash
    python plot_functions.py
    ```
3.  Run the CSV generation script to get the summary table:
    ```bash
    python generate_csv.py
    ```

The plots will be saved in the `plots/` directory, and the CSV file will be saved in the root directory of the project.

```
```
