def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) is 0:
        return (None, None)
    min = float('inf')
    max = float('-inf')
    for i in ints:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Edge case 1 - empty list
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")

# Edge case 2 - single value list
print ("Pass" if ((9, 9) == get_min_max([9])) else "Fail")

# Edge case 3 - negatives and positives
print ("Pass" if ((-100, 100) == get_min_max([-99, -100, 99, 100, 1, 4, 5, 6, -5, -4, -1])) else "Fail")
