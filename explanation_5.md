# Building a Trie in Python
Building a trie in python, I chose to use an internal data structure representation of trienode children being a dictionary because it offers constant time insertion and lookup. When inserting a word or finding a prefix in the trie, my algorithm ran in linear time because it just iterated over the input. For finding the suffix's it also ran in linear time as it used depth first searching and only iterated over each inserted element in the children nodes once.

TrieNode::insert():
Runtime Complexity O(1)
Storage Complexity O(1)

TrieNode::suffixes():
Runtime Complexity O(n) - n is all the children in the tree.
Storage Complexity O(n) - n is all potential children in the tree.

Trie::insert():
Runtime Complexity O(n)
Storage Complexity O(1)

Trie::find():
Runtime Complexity O(n)
Storage Complexity O(1)