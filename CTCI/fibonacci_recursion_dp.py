
def recursive_f(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return recursive_f(i-1) + recursive_f(i-2)

print("Recursive solution : ", recursive_f(8))

def top_down_f(i):
    return f2(i, [0] * (i+1))

def f2(i, memo):
    if i == 0:
        return 0
    if i == 1:
        return 1

    if memo[i] == 0:
        memo[i] = f2(i-1, memo) + f2(i-2, memo)

    return memo[i]

print"Top down dp solution : ", (top_down_f(8))

def bottom_up_f(i):
    memo[0] = 0
    memo[1] = 1
    memo[i] =

print"Bottom up dp solution : ", (top_down_f(8))