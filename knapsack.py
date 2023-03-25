# the knapsack problem

def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity - weights[idx], idx+1)

        return max(option1, option2)


tst0 = { "input":{
    'weights':[23,31,29,44,53,38,63,85,89,82],
    'profits':[92,57,49,68,60,43,67,84,87,72],
    'capacity':165,
},
"output":309
}
tst1 = {
    "input":{
    'weights':[4,5,6],
    'profits':[1,2,3],
    'capacity':3,
    },
"output":0
}
tst2 = {
    "input":{
    'weights':[4,5,1],
    'profits':[1,2,3],
    'capacity':4
    },
"output":3
}
tst3 = {
    "input":{
    'weights':[41,50,49,59,55,57,60],
    'profits':[442,525,511,593,546,564,617],
    'capacity':170
    },
"output":1735
}
tst4 = {
    "input":{
    'weights':[4,5,6],
    'profits':[1,2,3],
    'capacity':15
    },
"output":6
}
tst5 = {
    "input":{
    'weights':[4,5,1,3,2,5],
    'profits':[2,3,1,5,4,7],
    'capacity':15
    },
"output":19
}

knapsack_tests = [tst0, tst1, tst2, tst3, tst4, tst5]

def evaluate_test_cases(function, tests):
    
    for test in tests:
        print("# Test Case:", tests.index(test) )
        result = function(**test["input"])

        if result == test["output"]:
            print("PASSED!\n","Expected output:", test["output"],"\n" "Actual output:", function(**test["input"]))
        else:
            print("FAILED!\n","Expected output:", test["output"],"\n" "Actual output:", function(**test["input"]))

#evaluate_test_cases(max_profit_recursive, knapsack_tests)

# personal challenge, implement the memory solution

# lets also implement the dynamic solution

def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)]for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], profits[i] + table[i][c-weights[i]])
    
    return table[-1][-1]

evaluate_test_cases(max_profit_dp, knapsack_tests)
