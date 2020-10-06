# Finding the Square Root of an Integer
I used binary search to determine the square root of the number. I caught some edge cases to exit early if need be (negative numbers, early numbers that would return 1). I then started with the upper bound of a number at half the size of the total possible numbers considering that half is a good starting point for checking as the earliest square root of an integer could be is half the size (sqrt(4) == 2).
The runtime is O(log(n))
The space complexity is O(1)