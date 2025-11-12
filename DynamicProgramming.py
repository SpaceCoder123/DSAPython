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

class DynamicProgramming:
    def knapsackRec(self, W, val, wt, n):
        if n == 0 or W == 0:
            return 0
        pick = 0
        if wt[n - 1] <= W:
            pick = val[n - 1] + self.knapsackRec(W - wt[n - 1], val, wt, n - 1)
        notPick = self.knapsackRec(W, val, wt, n - 1)
        
        return max(pick, notPick)

    # def isMatch(self, s, p):
    #     funcLen = len(p)
    #     strLen = len(s)
    #     if p == "*":
    #         return True
    #     def isMatchHelper(strIndex, funcIndex):
    #         print(strIndex, funcIndex)
    #         if strIndex >= strLen or funcIndex >= funcLen:
    #             if funcIndex >= funcLen-1 and strIndex >= strLen-1 :
    #                 return True
    #             else:
    #                 return False
            
    #         if p[funcIndex] == "*":
    #             prevChar = s[funcIndex - 1]

    #             while(strIndex < strLen - 1  and s[strIndex] == prevChar):
    #                 strIndex+=1
    #             return isMatchHelper(strIndex+1, funcIndex+1)

    #         if (s[strIndex] != p[funcIndex]):
    #             if (strIndex >= strLen-1 or funcIndex >= funcLen - 1):
    #                 return False

    #         if s[strIndex] == p[funcIndex]:
    #             return isMatchHelper(strIndex+1, funcIndex+1)

    #         return isMatchHelper(strIndex+1, funcIndex+1)
        
    #     return isMatchHelper(0, 0)

    def longestCommonSubsequence(self, text1, text2):
        memo = {}
        def helper(idx1, idx2):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            
            if text1[idx1] == text2[idx2]:
                value = 1 + helper(idx1+1, idx2+1)
            else:
                value = max(helper(idx1, idx2+1), helper(idx1+1, idx2))
            memo[(idx1, idx2)] = value
            return value
        return helper(0,0)