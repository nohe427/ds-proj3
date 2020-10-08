# Search in a Rotated Sorted Array
In a rotated array search, I used a divide and conquer technique to divide the two lists into smaller sublists. If the lower index value was greater than the upper index value, I would recursively call the search function. If the lower index value was less than the upper index value, I knew I was in a sorted array and then perform binary search as expected.

Runtime O(log(n)) (this is if the array is actually rotated and not totally reversed)

Space complexity O(n^(log(n))) - Since this is a recursive function, I am bound by the amount of recursive calls. This means that while I recurse over the array, I am passing a copy of the array to each new stack frame which copies the entire array (input n) over. Since we know the runtime efficiency is log(n), the amount of times the input would be copied in a recursive call is log(n) times. 