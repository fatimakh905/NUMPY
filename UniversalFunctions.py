import numpy as np
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])

greater_result = np.greater(a, b)    # Element-wise comparison: a > b
less_result = np.less(a, b)          # Element-wise comparison: a < b
equal_result = np.equal(a, b)        # Element-wise comparison: a == b

a = np.array([True, False, True])
b = np.array([False, False, True])

and_result = np.logical_and(a, b)    # Element-wise logical AND
or_result = np.logical_or(a, b)      # Element-wise logical OR
not_result = np.logical_not(a)       # Element-wise logical NOT

values = np.array([-1.7, -0.2, 3.6, 1.5])

sqrt_result = np.sqrt([1, 4, 9, 16])   # Element-wise square root
abs_result = np.abs(values)            # Element-wise absolute value
round_result = np.round(values)        # Element-wise rounding to nearest integer

data = np.array([1, 2, 3, 4, 5])

sum_result = np.sum(data)              # Sum of all elements
prod_result = np.prod(data)            # Product of all elements
min_result = np.min(data)              # Minimum of all elements
max_result = np.max(data)              # Maximum of all elements

values = np.array([1.5, 2.3, 3.1])

floor_result = np.floor(values)        # Element-wise floor (round down)
ceil_result = np.ceil(values)          # Element-wise ceiling (round up)
