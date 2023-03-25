# finding the number of times a rotated sorted list was rotated

def count_rotations():
    pass
tests = []
# come up with some test input and output values
#test = {
#"input":{
#    "nums" : [5, 6, 1, 2, 3, 4, ]
#    },
#"output":2
#}
# edge cases 
# list was rotated once
# half the list was rotated
# list was not rotated 
# list with only one element
# list was rotated n - 1 times

tests.append({
    "input":{
        "nums":[10, 2, 4, 5, 6, 8, 9]},
        "output":1})

tests.append({
    "input":{
        "nums":[8, 9, 10, 2, 4, 5, 6]},
        "output":3})

tests.append({
    "input":{
        "nums":[2, 4, 5, 6, 8, 9, 10]},
        "output":0})

tests.append({
    "input":{
        "nums":[2]},
        "output":0})
# we create a test function to test our cases

def evaluate_test(count_rotations, test):

    result = count_rotations(**test["input"])

    if result == test["output"]:
        print("TRUE! test passed")
    else:
        print("FALSE! test failed")

# a function to evaluate test cases

def evaluate_test_cases(count_rotations_linear, tests):
    
    for test in tests:
        print("# Test Case:", tests.index(test) )
        result = count_rotations_linear(**test["input"])

        if result == test["output"]:
            print("PASSED!\n" "Tested list:", test["input"]["nums"], "\n" "Actual rotations counted:", result, "\n" "Expected rotations:", test["output"])
        else:
            print("FAILED!\n" "Tested list:", test["input"]["nums"], "\n" "Actual rotations counted:", result, "\n" "Expected rotations:", test["output"])

# we create a linear function

def count_rotations_linear(nums):
    position = 0
    
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1
    return 0

#print(count_rotations_linear(**test["input"]))

#evaluate_test(count_rotations_linear, test)

evaluate_test_cases(count_rotations_linear, tests)

# implementing the binary search