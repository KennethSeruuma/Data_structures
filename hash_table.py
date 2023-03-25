# implement a hash table class which supports the following operations
# insert: insert a new key-value pair
# find: find the value associated with a key
# update: update the value associated with a key
# list: list all the keys stored in the hash table
MAX_HASH_TABLE_SIZE = 4096

data_list = [None] * 4096

#print(len(data_list) == 4096)

#print(data_list[69]==None)

# a hushing function: is used to convert strings and other non numeric data types into numbers, 
# which can then be used as list indices, e.g, if the hash function converts 'kenny' into 4, then 
# the key-value pair ('kenny', 0176484) will be stored at position 4 within the data list

# a hashing algorithm:
# 1. iterate over the string, character by character
# 2. convert each character to a number using python's built-in ord function 
# 3. add the numbers for each character to obtain the hash for the entire string
# 4. take the remainder of the result with the size of the data list 

#print(ord('f'))

def get_index(data_list, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number 
    list_index = result % len(data_list)
    return list_index

def find(data_list, key):
        idx = get_valid_index(data_list, key)
        kv = data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value

def insert(data_list, key, value):
        idx = get_valid_index(data_list, key)
        data_list[idx] = key, value

def list_all():
        return [kv[0] for kv in data_list if kv is not None]      
#print(get_index(data_list, 'kenneth'))

data_list2 = [None] * 48
#print(get_index(data_list2, 'Aakash'))

#print(ord('A')+ord('a')+ord('k')+ord('a')+ord('s')+ord('h'))

# storing a key-value pair using the hash function

idx = get_index(data_list, 'Aakash')
data_list[idx] = ('Aakash', '00897398')
# same as 
data_list[get_index(data_list, 'kenneth')] = ('kenneth', '897398')
# likewise accessing key-value pairs

idx1 = get_index(data_list, 'Aakash')
key, value = data_list[idx1]
# alternatively
#key, value = data_list[get_index(data_list, 'Aakash')]

# a simple list comprehension

pairs = [kv[0] for kv in data_list if kv is not None] # gives a list of keys

#print(pairs)

class basichashtable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None]*max_size
    
    def insert(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = get_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]

basic_table = basichashtable(max_size=1024)
basic_table.insert('jammy', '093782')
basic_table.insert('reagan', '7658729')
basic_table.insert('john', '02846')

#print(basic_table.find('jammy'))
basic_table.update('john', '7777777')
#print(basic_table.find('john'))
#print(basic_table.list_all())

def get_valid_index(data_list, key):
    # start with the index returned by the get_index function
    idx = get_index(data_list, key)
    while True:
        # get the key-value pair stored at the idx position
        kv = data_list[idx]
        # if it is None, return the index
        if kv is None:
            return idx
        # if the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        # move to the next index
        idx += 1
        # go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0
       
data_list3 = [None] * MAX_HASH_TABLE_SIZE
#print(get_valid_index(data_list3, 'listen'))
data_list3[get_index(data_list3, 'listen')] = ('listen', '444444')
#print(get_valid_index(data_list3, 'silent'))

# lets now implement a hash table with linear probing

class probinghashtable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None]*max_size
    
    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
# we can test our probing class

probing_table = probinghashtable()
probing_table.insert('listen', 4444)
probing_table.insert('silent', 6666)
#print(probing_table.find('listen'))
probing_table.update('listen', 7777)
#print(probing_table.find('listen'))
#print(probing_table.list_all())

# implement a pyhton friendly user interface for a hash table

class friendlyHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None]*max_size
    def get_valid_index(self, key):
        idx = get_index(data_list, key)
        while True:
            kv = data_list[idx]
            if kv is None:
                return idx
            k, v = kv
            if k == key:
                return idx
            idx += 1
            if idx == len(data_list):
                idx = 0
    def __getitem__(self, key):
        value1 = find(self.data_list, key)
        return value1
    def __setitem__(self, key, value):
        insert(self.data_list, key, value)
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    def __len__(self):
        return ([x for x in self])
    def __repr__(self):
        from textwrap import indent
        kv = self.data_list[idx]
        pairs = [indent("{}:{}".format(repr(kv[0]), repr(kv[1]), ''))]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    def __str__(self):
        return repr(self)
# we wld hv to use a function hush(), hush('keno') % len(data_list)

newHash = friendlyHashTable()
newHash['kent'] = 'kent', 26764
newHash['merix'] = 'merix', 89756
newHash['joe'] = 'joe', 31425

print(newHash['merix'])
newHash['merix'] = 'merix', 66666
print(newHash['merix'])
#print(newHash)
