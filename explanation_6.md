# Max and Min in a Unsorted Array
I used a maximum and minimum value that are outside the bounds of any potential integer for a starting base. This allowed me to cover edge cases of huge integers. From there, I just iterated over the list of integers and checked if they were less than my previous min or more than my previous max and if they were I would set it to that value. This allowed me to iterate over the list only once.

Runtime Complexity O(n)

Space Complexity O(1)