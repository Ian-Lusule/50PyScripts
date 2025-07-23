```python
# python-mini-projects/random_number_generator.py

import random
import argparse
import numpy as np
from scipy.stats import norm, expon

def generate_uniform(min_val, max_val, num_samples):
    """Generates a list of uniformly distributed random numbers.

    Args:
        min_val: The minimum value (inclusive).
        max_val: The maximum value (inclusive).
        num_samples: The number of random numbers to generate.

    Returns:
        A list of uniformly distributed random numbers.  Returns None if input is invalid.
    """
    if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)) or not isinstance(num_samples, int):
        print("Error: min_val, max_val must be numbers, num_samples must be an integer.")
        return None
    if num_samples <=0:
        print("Error: num_samples must be positive.")
        return None
    if min_val > max_val:
        print("Error: min_val cannot be greater than max_val.")
        return None

    return [random.uniform(min_val, max_val) for _ in range(num_samples)]


def generate_normal(mean, std_dev, num_samples):
    """Generates a list of normally distributed random numbers.

    Args:
        mean: The mean of the normal distribution.
        std_dev: The standard deviation of the normal distribution.
        num_samples: The number of random numbers to generate.

    Returns:
        A list of normally distributed random numbers. Returns None if input is invalid.
    """
    if not isinstance(mean, (int, float)) or not isinstance(std_dev, (int, float)) or not isinstance(num_samples, int):
        print("Error: mean, std_dev must be numbers, num_samples must be an integer.")
        return None
    if num_samples <= 0:
        print("Error: num_samples must be positive.")
        return None
    if std_dev <= 0:
        print("Error: Standard deviation must be positive.")
        return None

    return [random.gauss(mean, std_dev) for _ in range(num_samples)]


def generate_exponential(lambda_param, num_samples):
    """Generates a list of exponentially distributed random numbers.

    Args:
        lambda_param: The rate parameter (lambda) of the exponential distribution.
        num_samples: The number of random numbers to generate.

    Returns:
        A list of exponentially distributed random numbers. Returns None if input is invalid.
    """
    if not isinstance(lambda_param, (int, float)) or not isinstance(num_samples, int):
        print("Error: lambda_param must be a number, num_samples must be an integer.")
        return None
    if num_samples <= 0:
        print("Error: num_samples must be positive.")
        return None
    if lambda_param <= 0:
        print("Error: Lambda parameter must be positive.")
        return None

    return [random.expovariate(lambda_param) for _ in range(num_samples)]


def main():
    parser = argparse.ArgumentParser(description="Generate random numbers with various distributions.")
    parser.add_argument("distribution", choices=["uniform", "normal", "exponential"], help="The type of distribution.")
    parser.add_argument("num_samples", type=int, help="The number of random numbers to generate.")
    parser.add_argument("params", nargs="+", help="Distribution parameters (min, max for uniform; mean, stddev for normal; lambda for exponential).")

    args = parser.parse_args()

    if args.distribution == "uniform":
        if len(args.params) != 2:
            print("Error: Uniform distribution requires two parameters (min, max).")
            return
        min_val, max_val = map(float, args.params)
        result = generate_uniform(min_val, max_val, args.num_samples)

    elif args.distribution == "normal":
        if len(args.params) != 2:
            print("Error: Normal distribution requires two parameters (mean, stddev).")
            return
        mean, std_dev = map(float, args.params)
        result = generate_normal(mean, std_dev, args.num_samples)

    elif args.distribution == "exponential":
        if len(args.params) != 1:
            print("Error: Exponential distribution requires one parameter (lambda).")
            return
        lambda_param = float(args.params[0])
        result = generate_exponential(lambda_param, args.num_samples)

    if result:
        print(result)


if __name__ == "__main__":
    main()
```