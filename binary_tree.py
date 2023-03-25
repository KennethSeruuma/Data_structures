class user:
    
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.username}(username = {self.username}, name = {self.name}, email = {self.email})".format(user)
    def __str__(self):
        return self.__repr__()

class user_database():
    
    def __init__(self):
        self.users = []

    def __repr__(self):
        return f"(username={user.username}, user={user})".format(user_database)
    def __str__(self):
        return self.__repr__()
    def insert_profile(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    def find_profile(self, username):
        for user in self.users:
            if user.username == username:
                return user
    def update_profile(self, user):
        target = self.find_profile(user.username)
        target.name, target.email = user.name, user.email
        
    def list_users(self):
        return self.users

class treenode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(treenode.height(self.left), treenode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + treenode.size(self.left) + treenode.size(self.right)
    
    def traverse_in_order(self):
        if self is None:
            return []
        return (treenode.traverse_in_order(self.left) + [self.key] + treenode.traverse_in_order(self.right))

    def display_keys(self, space='\t', level = 0):
    
        if self is None:
            print(space*level + "Q")
            return
    
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
    
        treenode.display_keys(self.left, space, level + 1)
        print(space*level + str(self.key))
        treenode.display_keys(self.right, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        return treenode.to_tuple(self.left), self.key, treenode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = treenode(data[1])
            node.left = treenode.parse_tuple(data[0])
            node.right = treenode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = treenode(data)

        return node

tree_tuple = ((1, 3, None), 2, ((None, 4, 5), 6, (7, 8, 9)))

tree = treenode.parse_tuple(tree_tuple)
#print(tree)
#treenode.display_keys(tree)
#print(treenode.height(tree))
#print(treenode.size(tree))
#print(treenode.traverse_in_order(tree))
#print(treenode.to_tuple(tree))

# a function to determine whether a binary tree is a bst
# it also returns the minimum and maximum keys
def remove_none(num1, num2, num3):
   
    return (x for x in (num1, num2, num3) if x is not None )

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = ( is_bst_l and is_bst_r and
                    (max_l is None or node.key > max_l) and 
                    (min_r is None or node.key < min_r))

    min_key = min(remove_none(min_l, node.key, min_r))
    max_key = max(remove_none(max_l, node.key, max_r))

    return is_bst_node, min_key, max_key

#print(is_bst(tree))

# storing key-values pairs using bsts 

class bstnode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
    
    def __repr__(self):
        return f"{self.value}".format(bstnode)
    def __str__(self):
        return self.__repr__()

allen = user("allen", "allen naki", "allenak@gits.com")
beth = user("beth", "beth namu", "bethna@holly.com")
cathy = user("cathy", "cathy jo", "cathyjo@wothry.com")
dick = user("dick", "dick fat", "dickf@means.com")
emma = user("emma", "emma seri", "emmas@hanks.com")
james = user("james", "james jo", "jajo@kitts.com")
kenio = user("kenio", "kenio one", "ken@html.com")
lameti = user("lameti", "lameti adams", "lamads@true.com")
men = user("men", "men hanks", "menhk@wothry.com")
opio = user("opio", "opio dan", "opda@calm.com")

print(allen)

database = user_database()
database.insert_profile(allen)
database.insert_profile(beth)
database.insert_profile(cathy)
database.insert_profile(dick)
database.insert_profile(emma)
database.insert_profile(james)
database.insert_profile(kenio)
database.insert_profile(lameti)
database.insert_profile(men)
database.insert_profile(opio)

tree1 = bstnode(dick.username, dick)
#print(tree1.key, tree1.value)
tree1.left = bstnode(beth.username, beth)
tree1.left.parent = tree1
tree1.right = bstnode(james.username, james)
tree1.right.parent = tree1

tree1.left.left = bstnode(allen.username, allen)
tree1.left.right = bstnode(cathy.username, cathy)
tree1.right.left = bstnode(emma.username, emma)
tree1.right.right = bstnode(kenio.username, kenio)

#treenode.display_keys(tree1)
#print(is_bst(tree1))

# a function to insert into a bst
def insert_in_bst(node, key, value):
    if node is None:
        node = bstnode(key, value)
    elif key < node.key:
        node.left = insert_in_bst(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert_in_bst(node.right, key, value)
        node.right.parent = node
    return node

insert_in_bst(tree1, men.username, men)
insert_in_bst(tree1, lameti.username, lameti)
insert_in_bst(tree1, opio.username, opio)
#treenode.display_keys(tree1)

# a function to find a value in a bst
def find_in_bst(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find_in_bst(node.left, key)
    if key > node.key:
        return find_in_bst(node.right, key)

#print(find_in_bst(tree1, allen.username))

# a function to update a value associated with a given key in a bst
def update_bst(node, key, value):
    target = find_in_bst(node, key)
    if target is not None:
        target.value = value

#update_bst(tree1, kenio.username, user("keny", "keny one", "ken@html.com"))
#print(find_in_bst(tree1, kenio.username))

# a function to list all the key-value pairs in the bst
def list_all_bst(node):
    if node is None:
        return []
    return list_all_bst(node.left) + [(node.key, node.value)] + list_all_bst(node.right)

#print(list_all_bst(tree1))

# a function to determine if a given bst is balanced
def is_balanced_bst(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced_bst(node.left)
    balanced_r, height_r = is_balanced_bst(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height
#treenode.display_keys(tree1)
#print(is_balanced_bst(tree1))

# a function to create a balanced binary tree from a sorted list of key-value pairs
def create_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    key, value = data[mid]
    root = bstnode(key, value)
    root.parent = parent
    root.left = create_balanced_bst(data, lo, mid-1, root)
    root.right = create_balanced_bst(data, mid+1, hi, root)

    return root

data = [(user.username, user) for user in database.users]
#print(data)
#tree2 = create_balanced_bst(data)
#treenode.display_keys(tree2)

#print(is_balanced_bst(tree2))

# remember that direct insertion of one by one in sorted order, 
# only results in a skew. see below;
tree3 = None
for username, user in data:
    tree3 = insert_in_bst(tree3, username, user)

#print(list_all_bst(tree3))
#treenode.display_keys(tree3)
#print(is_balanced_bst(tree3))

# how to balance an unbalanced binary tree

def balance_bst(node):
    return create_balanced_bst(list_all_bst(node))

tree4 = balance_bst(tree3)
#treenode.display_keys(tree4)

# consider creating a generic class treemap which simplifies data entry to user

class treemap():
    def __init__(self):
        self.root = None
    def __setitem__(self, key, value):
        node = find_in_bst(self.root, key)
        if not node:
            self.root = insert_in_bst(self.root, key, value)
            self.root = balance_bst(self.root)# we can perform the balancing at 
            # every certain inserting intervals say every after 1000 insertions
        else:
            update_bst(self.root, key, value)
    def __getitem__(self, key):
        node = find_in_bst(self.root, key)
        return node.value if node else None
    def __iter__(self):
        return (x for x in list_all_bst(self.root))
    def __len__(self):
        return treenode.size(self.root)
    def display(self):
        return treenode.display_keys(self.root)

treemap1 = treemap()
#print(treemap1.root)
print(allen)
# adding elements
treemap1['kenio'] = kenio
treemap1['allen'] = allen
treemap1['opio'] = opio

#treemap1.display()
#print(allen)
# retrieving elements
#print(treemap1['allen'])
#print(treemap1['kenio'])

# more to try out
# implement rotatons and self balancing insertions
# implement deletion of a node from a binary search tree
# implement deletion of a node from a bst (with balancing)
# find the lowest common ancestor of two nodes in a tree(hint: use the parent property)
# find the next node in lexicographic order for a given node
# given a number k, find the k-th node in a bst