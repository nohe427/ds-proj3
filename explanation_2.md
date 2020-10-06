# Search in a Rotated Sorted Array
In a rotated array search, I used a divide and conquer technique to divide the two lists into smaller sublists. If the lower index value was greater than the upper index value, I would recursively call the search function. If the lower index value was less than the upper index value, I knew I was in a sorted array and then perform binary search as expected.
Runtime O(log(n)) (this is if the array is actually rotated and not totally reversed)
Space complexity O(n)