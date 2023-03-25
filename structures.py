
def locate_card_():
    pass

# lets form a list to contain all edge cases

tests = []

tests.append({"input" : {
    "cards" : [11, 9, 7, 6, 5, 3],
    "querry" : 5
},
"output" : 4
})

# card is the first element

tests.append({"input" : {
    "cards" : [4, 3, 2, 1],
    "querry" : 4
},
"output" : 0
})

# card is the last element

tests.append({"input":{
    "cards":[7, 5, 3, 2],
    "querry": 2
},
"output" : 3
})

# there is only one element, the querry

tests.append({"input":{
    "cards":[3],
    "querry": 3
},
"output": 0
})

# the list is empty

tests.append({"input":{
    "cards":[],
    "querry": 3
},
"output": None # make a reasonable assumption, e.g, output cld be -1
})

# the list does not contain querry

tests.append({"input":{
    "cards":[8, 7, 7, 7, 3, 2],
    "querry": 5
},
"output": None # again, reasonable assumption
})

# there are repeating elements

tests.append({"input":{
    "cards":[8, 7, 7, 7, 3, 2],
    "querry": 3
},
"output": 4
})

# the querry occurs more than once

tests.append({"input":{
    "cards":[8, 7, 5, 3, 3, 2],
    "querry": 3
},
"output": 3 # again make it determinist, e.g, return first position
})

tests.append({"input":{
    "cards":list(range (1000000, 0, -1)),
    "querry": 2
},
"output": 999998 # again make it determinist, e.g, return first position
})
# lets create our linear search function
def locate_card_linear(cards, querry):
    position = 0

    while position < len(cards):

        if cards[position] == querry:
            return position
        position += 1
    return None

# its more convinient to create a small function to test the edge case
# or a fuction to test edge cases

# this function tests whether the position of querry is 
# the first position, for recurring querry
def test_location(cards, querry, mid):
    
    mid_value = cards[mid]
    
    if mid_value == querry:
        if mid - 1 >= 0 and cards[mid - 1] == querry:
            return "left"
        else:
            return "found"
    elif mid_value < querry:
            return "left"
    else:
        return "right"

# we create the binary search function
def locate_card_binary(cards, querry):

    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        
        result = test_location(cards, querry, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return None

def evaluate_test_case(locate_card_binary, test):

    result = locate_card_binary(**test["input"])

    if result == test["output"]:
        print("TRUE! test passed")
    else:
        print("FALSE! test failed")

# we need to create a function that tests all the test cases
def evaluate_test_cases(locate_card_binary, tests):
    
    for test in tests:
        print("# Test Case:", tests.index(test) )
        result = locate_card_binary(**test["input"])

        if result == test["output"]:
            print("PASSED!\n" "querry:", test["input"]["querry"], "Found at position:", result, "Expeceted position:", test["output"])
        else:
            print("FAILED!\n" "querry:", test["input"]["querry"], "Found at position:", result, "Expected position", test["output"])


evaluate_test_cases(locate_card_linear, tests)

#super().__init__(
#            self.name, self.username, self.email
#        )

