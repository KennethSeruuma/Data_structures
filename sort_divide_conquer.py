# some list of numbers in random order
# a list that is already sorted
# a list that is sorted in decreasing order
# a list containting repeating elements
# an empty list
# a list containing just one element
# a list containing one element repeated many times 
# a really long list
import random
def sort():
    pass

# test case 0
test0 = {"input": {"nums":[3,8,6,4,9,1,2]},
                "output": [1,2,3,4,6,8,9]}
# test case 1
test1 = {"input": {"nums":[9,8,6,4,3,2,1]},
                "output": [1,2,3,4,6,8,9]}
# test case 2
test2 = {"input": {"nums":[1,2,3,4,6,8,9]},
                "output": [1,2,3,4,6,8,9]}
# test case 3
test3 = {"input": {"nums":[1,2,6,8,2,9,2]},
                "output": [1,2,2,2,6,8,9]}
# test case 4
test4 = {"input": {"nums":[8]},
                "output": [8]}
# test case 5 
test5 = {"input": {"nums":[2,2,2,2,2,2,2]},
                "output": [2,2,2,2,2,2,2]}
#test case 6
test6 = {"input":{"nums":[]},
                "output":[]}

in_list = list(range(1000))
out_list = list(range(1000))
#print(in_list)
random.shuffle(in_list)
#print(in_list)
test7 = {"input": {"nums":in_list},
                "output": out_list}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

def buble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums              

def evaluate_test_cases(function, tests):
    
    for test in tests:
        print("# Test Case:", tests.index(test) )
        result = function(**test["input"])

        if result == test["output"]:
            print("PASSED!\n" "Tested list:", test["input"]["nums"], "\n" "Actual output:", function(test["input"]["nums"]), "\n" "Expected output:", test["output"])
        else:
            print("FAILED!\n" "Tested list:", test["input"]["nums"], "\n" "Actual output:", function(test["input"]["nums"]), "\n" "Expected output:", test["output"])

#evaluate_test_cases(buble_sort, tests)

def insert_sort(nums):
    nums = list(nums)# we copy the list to avoid changing it
    for i in range(len(nums)): # we iterate through the list 
        cur = nums.pop(i) # we chose an arbitrary value, which in this case is at the end of the list
        j = i - 1 # a subscript to compare the i value with the value jst before it
        while j >= 0 and nums[j] > cur: # we check for the first occuring position where
                                        # current value is greater than the value at that position
            j -= 1                   
        nums.insert(j + 1, cur) # we insert current value at that position
    return nums # we return a sorted list

#evaluate_test_cases(insert_sort, tests)

# determine the time and space complexity of insert sort 
# and see if it is any better than buble sort

# the divide and conquer techinique
def merge():
    pass
def merge_sort(nums):
    if len(nums) <= 1: # terminating condition, list of zero or one element
        return nums
    mid = len(nums) // 2 # get the mid point
    # split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    # solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    # combine the results of the two halves
    merge_sorted = merge(left_sorted, right_sorted)
    return merge_sorted

def merge(nums1, nums2):
    merged = [] # creat an empty list were to add compared values
    i, j = 0, 0 # initialise pointer indices at zero
    # we loop through the lists
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    # we obtain the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    # return the merged final array
    return merged + nums1_tail + nums2_tail

#nums1, nums2 = [1,4,6,7,9], [2,3,5,8]
#print(merge(nums1, nums2))

#evaluate_test_cases(merge_sort, tests)

# the quick sort algorithm
def partition():
    pass
def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot + 1, end)
    return nums

def partition(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    l, r = start, end - 1
    while r > l:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

#nm = [3, 2, 1, 7, 0, 8, 4]
#pivot = partition(nm)
#nm1 = quick_sort(nm)
#print(nm, nm1, pivot)
#evaluate_test_cases(quick_sort, tests)

# wirte a function to sort a list of notebooks in decreasing order of likes,
# keep in mind that up to millions of notebooks can be created every week,
# so your function needs to be as efficient as possible

#  lets write a class that captures basic information about notebooks

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
    def __repr__(self):
        return 'Notebook<"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
# lets create some cases of notebooks
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]
# lets write a customs comparison function to compare two notebooks
def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return "lesser" # bse nb1 has more likes than nb2 and we r sorting in decending order
    elif nb1.likes == nb2.likes:
        return "equal"
    elif nb1.likes < nb2.likes:
        return "greater"
#print(notebooks)

# check out this default compare function
def default_compare(x, y):
    if x < y:
        return 'lesser'
    elif x == y:
        return 'equal'
    else:
        return 'greater'
def merge_sort_objs(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge_objs(merge_sort_objs(objs[:mid], compare),
                      merge_sort_objs(objs[mid:], compare),
                      compare)
def merge_objs(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

#print(merge_sort_objs(notebooks, compare_likes))

# since we hv written a generic merge_sort 
# function that works with any compare function
# we can now use it to sort notebooks by title

def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title > nb2.title:
        return 'greater'

#print(merge_sort_objs(notebooks, compare_titles))

def compare_usernames(nb1, nb2):
    if nb1.username < nb2.username:
        return 'lesser'
    elif nb1.username == nb2.username:
        return 'equal'
    elif nb1.username > nb2.username:
        return 'greater'

#print(merge_sort_objs(notebooks, compare_usernames))