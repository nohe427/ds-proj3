# HTTPRouter using a Trie

This project largely used the same implementation as problem 5. I used a dictionary to store all root paths because it offers constant lookup and insertion time. When inserting new paths and handlers, the insertion ran in linear time because it needed to iterate over the input. I did not use the split_path method in the Router as I implemented split path elsewhere and did not see that method until later.

Runtime Complexity : O(n)

Storage Complexity : O(nSS)