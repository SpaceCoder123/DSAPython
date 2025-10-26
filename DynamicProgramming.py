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


def knapsack(knapWeight, n, weights, values):
    if n == 0 or knapWeight == 0:
        return 0
    
    if weights[n] <= knapWeight:
        return max(values[n] + knapsack(knapWeight-weights[n], n-1, weights, values), knapsack(knapWeight, n-1, weights, values))

    else:
        return knapsack(knapWeight, n-1, weights, values)
    
weights = [4, 5, 6]
profit = [1, 2, 3]
knapWeight = 3
n = len(weights)

print(knapsack(knapWeight, n-1, weights, profit))