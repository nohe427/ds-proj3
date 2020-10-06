def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    end = len(input_list)-1
    i = 0
    # Needs to be less than the end so it doesn't swap portions of the already sorted array.
    # Also needs to be less than or equal to in order to evaluate correctly.
    while i <= end:
        v = input_list[i]
        if v == 0:
            swap(input_list, start, i)
            start+=1
            i+=1
        elif v == 2:
            swap(input_list, end, i)
            end-=1
        else:
            i+=1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge case 1 - Empty Array
test_function([])

# Edge case 2 - Reversed Array
test_function([2,2,2,2,2,2,2,1,1,1,1,1,0,0,0,0,0,0])

# Edge case 3 - Single Item Array
test_function([1])