# knapsack problem

# major points to consider for solving dynammic programming problems
# base condition
# choice diagram
# maximum value may not be greedy solution but will be an optimal solution

# identification of the dynamic programming problem
# identify whether a choice is present when you break the problem into smaller problem


# types of knapsack problems
# fractional knapsack ( fraction of the item can be added to the knapsack to extract maximum value )
# 0-1 knapsack ( complete item can be added or else the complete item must be discarded )
# unbounded knapsack ( repeated items can be added multiple times in the knapsack )


# procedure of solving
# recursion
# memoization
# top down approach (optional)
    
weights = [4, 5, 6]
profit = [1, 3, 3]
knapWeight = 10
n = len(weights)

# print(knapsack(knapWeight, n-1, weights, profit))


def knapsackRec(W, val, wt, n):
    if n == 0 or W == 0:
        return 0
    pick = 0
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)
    notPick = knapsackRec(W, val, wt, n - 1)
     
    return max(pick, notPick)

print(knapsackRec(knapWeight, profit, weights, n))