def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) < 1:
        return -1

    lower = 0
    upper = len(input_list)-1

    return rotated_array_search_helper(input_list, lower, upper, number)

def rotated_array_search_helper(arr, lower_index, upper_index, number):
    mid_index = (lower_index + upper_index)//2

    if arr[mid_index] == number:
        return mid_index
    if lower_index >= mid_index:
        return -1

    # This is the sorted array pattern
    if arr[lower_index] < arr[upper_index]:
        # Exit early condition.
        if number not in range(arr[lower_index], arr[upper_index]):
            return -1
        if number > arr[mid_index]:
            return rotated_array_search_helper(arr, mid_index, upper_index, number)
        else:
            return rotated_array_search_helper(arr, lower_index, mid_index, number)
    
    # This is the rotated array pattern
    if arr[lower_index] > arr[upper_index]:
        return max(rotated_array_search_helper(arr, lower_index, mid_index, number), rotated_array_search_helper(arr, mid_index, upper_index, number))

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge case 1 - A fully rotated array
test_function([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 9])

# Edge case 2 - an Array with only one element
test_function([[2], 2])

# Edge case 3 - an Array with only zero elements
test_function([[], 2])