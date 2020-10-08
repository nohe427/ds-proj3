# HTTPRouter using a Trie

This project largely used the same implementation as problem 5. I used a dictionary to store all root paths because it offers constant lookup and insertion time. When inserting new paths and handlers, the insertion ran in linear time because it needed to iterate over the input. I did not use the split_path method in the Router as I implemented split path elsewhere and did not see that method until later.

RouteTrie::insert():
Runtime Complexity : O(n) - Calls split
Storage Complexity : O(n) - Calls split

RouteTrie::find()
Runtime Complexity : O(n) - Calls Split iterates over all parts down trie
Storage Complexity : O(n) - calls split which has storage of O(n)

RouteTrieNode::insert()
Runtime Complexity : O(n) - Calls split
Storage Complexity : O(n) - Calls split

Router::add_handler()
Runtime Complexity : O(n) - Calls insert which calls split
Storage Complexity : O(n) - Calls insert which calls split

Router::lookup()
Runtime Complexity : O(n) - Calls find which has runtime of O(n)
Storage Complexity : O(n) - Calls split which has storage of (n)

Router::split_path
Runtime Complexity : O(n) (pretty sure split iterates over all chars)
Storage Complexity : O(n) (New array is created with all split chars)

