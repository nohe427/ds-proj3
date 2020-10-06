# Using a cmp lambda so I can sort any way I want
# Read wiki page here for Lomuto partition scheme
# https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
def quicksort(arr, low, high, cmp):
    if low < high:
        pivot = partition(arr, low, high, cmp)
        quicksort(arr, low, pivot-1, cmp)
        quicksort(arr, pivot+1, high, cmp)

def partition(arr, low, high, cmp):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if cmp(arr[j], pivot):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i+=1
    tmp = arr[i]
    arr[i] = arr[high]
    arr[high] = tmp
    return i

# Test code that I used to ensure my quicksort function worked
# arr = [5,4,6,8,9,1,2,0,4,6,7]
# quicksort(arr, 0, len(arr)-1, lambda x, y : x > y)
# print(arr)

def appendInt(input, appendValue):
    newValue = str(input) + str(appendValue)
    return int(newValue)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # start by sorting the input list
    quicksort(input_list, 0, len(input_list)-1, lambda x, y : x > y)
    firstNum = 0
    secondNum = 0
    for i, v in enumerate(input_list):
        if i is 0 or i % 2 == 0:
            firstNum = appendInt(firstNum, v)
        else:
            secondNum = appendInt(secondNum, v)
    return [firstNum, secondNum]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

# Edge Case 1 - Array with single element
test_function([[1], [1, 0]])

# Edge Case 2 - Empty array
test_function([[], [0,0]])

# Case 3 - random array
test_function([[1,0,2,9,3,8,4,7,6,5], [97531,86420]])