# longest common sequence

def lcs_recursive (seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)

# test cases

t0 = {"input":{
'seq1': 'serendipitous',
'seq2':'precipitation'
},
"output": 7
}
t1 = {"input":{
'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
},
"output": 5
}
t2 = {"input":{
'seq1': 'longest',
'seq2': 'stone'
},
"output": 3
}
t3 = {"input":{
'seq1':'oplkijomnhji',
'seq2':'adfefcfxeeff'
},
"output": 0
}
t4 = {"input":{
'seq1':"dense",
'seq2': 'condensed'
},
"output": 5
}
t5 = {"input":{
    
'seq1': '',
'seq2':''},
"output": 0
}
t6 = {"input":{
'seq1': 'abcdef',
'seq2': 'bdceaf'
},
"output": 4
}
print(lcs_recursive(t0['input']['seq1'], t0['input']['seq2']))
lcs_tests = [t0, t1, t2, t3, t4, t5, t6]

def evaluate_test_cases(function, tests):
    
    for test in tests:
        print("# Test Case:", tests.index(test) )
        result = function(**test["input"])

        if result == test["output"]:
            print("PASSED!\n" "sequence 1:", test["input"]["seq1"], "\n" "sequence 2:", test["input"]["seq2"], 
                "\n" "Expected output:", test["output"],
                "\n" "Actual output:", function(test["input"]["seq1"], test["input"]["seq2"]))
        else:
            print("FAILED!\n" "sequence 1:", test["input"]["seq1"], 
                "\n" "sequence 2:", test["input"]["seq2"], "\n" "Expected output:", test["output"],
                "\n" "Actual output:", function(test["input"]["seq1"], test["input"]["seq2"]))

#evaluate_test_cases(lcs_recursive, lcs_tests)

# over coming enefficiencies, through memorisation

def lcs_memo(seq1, seq2):
    memo = {}
    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0, 0)

#evaluate_test_cases(lcs_memo, lcs_tests)

# the dynamic programming solution

def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    return table[-1][-1]

#evaluate_test_cases(lcs_dp, lcs_tests)