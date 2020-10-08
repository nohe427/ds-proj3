# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('', handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        patharr = path.split("/")
        node = self.root
        if patharr[-1] == "":
            patharr = patharr[0:-1]
        for part in patharr:
            node = node.insert(None, part)
        node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        patharr = path.split("/")
        node = self.root
        if patharr[-1] == "":
            patharr = patharr[0:-1]
        if len(patharr) == 1 and patharr[0] == "":
            return self.root
        for part in patharr:
            if part in node.children.keys():
                node = node.children[part]
            else:
                return None
        return node

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, path, handler = None):
        # Initialize the node with children as before, plus a handler
        self.path = path
        self.handler = handler
        self.children = dict()

    def insert(self, handler, path):
        # Insert the node as before
        node = RouteTrieNode(path, handler)
        found = None
        if path in self.children.keys():
            found = self.children[path]
        else:
            self.children[path] = node
            found = node
        return found


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.not_found_handler = not_found_handler
        self.root = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path[0] is not "/":
            print("ERROR: PATHS MUST START WITH A '/'")
            return
        self.root.insert(path, handler)
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        node = self.root.find(path)
        if node is None or node.handler is None:
            return self.not_found_handler
        else:
            return "Test: " + str(node.handler)


    # Implemented this method, but I am not going to use it because my RouteTrie handles this
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        patharr = path.split("/")
        if patharr[-1] == "":
            patharr = patharr[0:-1]
        return patharr



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Edge case 1 - long paths
print("\nEdge One")
router.add_handler("/cool/dude/dawg/stuff/neat/me", "me")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/cool/dude/dawg/stuff/neat/me/")) # should print "me"
print(router.lookup("/cool/dude/dawg/stuff/neat/")) # should print 'not found handler'
print(router.lookup("/cool/dude/dawg/stuff/neat/me")) # should print 'me'

# Edge case 2 - Empty router
print("\nEdge Two")
router = Router("root", "404")
print(router.lookup("/")) # prints 'root'
print(router.lookup("/anything")) # prints '404'

# Edge case 3 - short route
print("\nEdge Three")
router = Router("root", "404")
router.add_handler("/short", "short handle")
print(router.lookup("/short")) # Should print 'short handle'

# Edge case 4 - No starting slash
print("\nEdge Four")
router = Router("test", "error")
router.add_handler("nostartingslash", "hmmm") # Should print ERROR: PATHS MUST START WITH A '/'
print(router.lookup("nostartingslash")) # should print "error"