# Rearrange Array Elements
The way I solved this problem was that I used quicksort. I used the wikipedia article on quicksort for a straightforward guide on quicksort (https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme). The quicksort we used in the lessons left me a little confused. In using quicksort I additionally passed a comparator object that allows me to reuse the quicksort function as needed by being able to specify a function to do the comparing. While this is a one off assignment, I may want to reuse that function again elsewhere. Additionally, I chose quicksort for its in place sorting that allows for a space complexity of O(n) allowing me to pass very large arrays as input.

Runtime Complexity O(nlogn)

Space Complexity O(n)