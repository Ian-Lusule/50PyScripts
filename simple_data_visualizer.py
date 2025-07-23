```python
"""
simple_data_visualizer.py

A simple data visualizer using matplotlib.  Allows users to visualize data from a CSV file.
"""

import matplotlib.pyplot as plt
import pandas as pd
import argparse
import os

def visualize_data(filepath, x_col, y_col, chart_type):
    """
    Visualizes data from a CSV file using matplotlib.

    Args:
        filepath: Path to the CSV file.
        x_col: Name of the column to use for the x-axis.
        y_col: Name of the column to use for the y-axis.
        chart_type: Type of chart to generate ('line', 'scatter', 'bar').
    
    Raises:
        FileNotFoundError: If the CSV file is not found.
        ValueError: If the specified columns are not found in the CSV file or if an invalid chart type is specified.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If there's an error parsing the CSV file.

    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at '{filepath}'")
    except pd.errors.EmptyDataError:
        raise ValueError("Error: CSV file is empty.")
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Error parsing CSV file: {e}")


    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError(f"Error: Columns '{x_col}' or '{y_col}' not found in CSV file.")

    if chart_type == 'line':
        plt.plot(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Line Chart: {x_col} vs {y_col}")
    elif chart_type == 'scatter':
        plt.scatter(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    elif chart_type == 'bar':
        plt.bar(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Bar Chart: {x_col} vs {y_col}")
    else:
        raise ValueError("Error: Invalid chart type. Choose from 'line', 'scatter', or 'bar'.")

    plt.show()


def main():
    """
    Parses command-line arguments and visualizes data.
    """
    parser = argparse.ArgumentParser(description="Simple data visualizer using matplotlib.")
    parser.add_argument("filepath", help="Path to the CSV file")
    parser.add_argument("x_col", help="Name of the x-axis column")
    parser.add_argument("y_col", help="Name of the y-axis column")
    parser.add_argument("chart_type", choices=['line', 'scatter', 'bar'], help="Type of chart ('line', 'scatter', 'bar')")

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: File not found at {args.filepath}")
        return

    try:
        visualize_data(args.filepath, args.x_col, args.y_col, args.chart_type)
    except (FileNotFoundError, ValueError, pd.errors.ParserError, pd.errors.EmptyDataError) as e:
        print(e)


if __name__ == "__main__":
    main()

```