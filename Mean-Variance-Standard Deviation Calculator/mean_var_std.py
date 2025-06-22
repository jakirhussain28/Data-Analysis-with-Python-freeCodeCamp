import numpy as np

# Create a function named calculate() in mean_var_std.py that uses Numpy to output 
# the mean, variance, standard deviation, max, min, and sum of the 
# rows, columns, and elements in a 3 x 3 matrix.

def calculate(list):
    if len(list) != 9:
        raise ValueError("only 9 nums to be exist.")
    
    matrix = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]
    }

    return calculations
