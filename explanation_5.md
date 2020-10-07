# Building a Trie in Python
Building a trie in python, I chose to use an internal data structure representation of trienode children being a dictionary because it offers constant time insertion and lookup. When inserting a word or finding a prefix in the trie, my algorithm ran in linear time because it just iterated over the input. For finding the suffix's it also ran in linear time as it used depth first searching and only iterated over each inserted element in the children nodes once.

Runtime Complexity O(n)

Storage Complexity O(n)