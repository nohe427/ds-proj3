# Dutch National Flag Problem
The dutch national flag problem can be sorted via three pointers that move depending on the value supplied.  If the value is 0 you swap the roaming pointer with the start pointer and move both pointers forward. If the value is 2, you swap the end pointer and the roaming pointer and then decrement the end pointer. The roaming pointer shouldn't be moved because we still need to evaluate the moved pointer from the end in its new position in the center. If the value is 1, we just move the roaming pointer. The reason that we want to evalute while the roaming pointer is less than or equal to the end pointer is that if the roaming pointer is 2 and the end pointer is 2, we could continually swap pointers until they meet and then pass each other.

Storage complexity O(n)

Runtime Complexity O(n)