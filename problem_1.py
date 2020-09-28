def sqrt(number: int) -> int:
   """
   Calculate the floored square root of a number

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """

   try:
      number = int(number)
   except:
      return -1

    # The square root of a negative number is imaginary.
    # We live in the real world here.
   if number < 0:
      return -1
   
   # Catching some edge cases to exit early
   if number == 0:
      return 0
   if number in {1, 2, 3}:
      return 1

   lower = 1
   upper = number//2
   # Catches the sqrt of 4 case early
   if upper**2 == number:
      return upper

   mid = upper - lower
   
   while lower < upper:
      midS = mid**2
      if midS <= number and (mid+1)**2 > number:
         return mid
      if midS > number:
         upper = mid
      elif midS < number:
         lower = mid
      mid = (upper + lower)//2

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge case 1 - negative numbers return -1
print ("Pass" if  (-1 == sqrt(-800)) else "Fail")

# Edge case 2 - Integer passed in as a string
print ("Pass" if  (5 == sqrt("27")) else "Fail")

# Edge case 3 - A string input is passed
print ("Pass" if  (-1 == sqrt("abc")) else "Fail")