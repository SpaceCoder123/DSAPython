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

from collections import deque

class DynamicProgramming:
    def knapsackRec(self, W, val, wt, n):
        if n == 0 or W == 0:
            return 0
        pick = 0
        if wt[n - 1] <= W:
            pick = val[n - 1] + self.knapsackRec(W - wt[n - 1], val, wt, n - 1)
        notPick = self.knapsackRec(W, val, wt, n - 1)
        
        return max(pick, notPick)

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
    
    def longestPalindromicSubstring(self, string):
        start, end = 0,0
        for i in range(len(string)):
            left1, right1 = self.checkPalindrome(i, i)
            left2, right2 = self.checkPalindrome(i,i+1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return string[start:end+1]
    
    def checkPalindrome(self, center, string):
        left = center
        right = center
        while(left >= 0 and right < len(string) and string[left] == string[right]):
            left-=1
            right+=1
        return (left+1, right-1)

    #O(n) space -> stack and O(n) time, 
    def longestValidParentheses(self, s):
        stack = deque()
        stack.append((-1, -1))
        maxLen = 0

        for idx, char in enumerate(s):
            tos_char, tos_idx = stack[-1]

            if char == '(':
                stack.append((char, idx))
            else:
                if tos_char == '(':
                    stack.pop()
                    new_tos_char, new_tos_idx = stack[-1]
                    maxLen = max(maxLen, idx - new_tos_idx)

                else:
                    stack.append((char, idx))
        return maxLen

    #O(n) time and O(1) space
    def longestValidParentheses(self, s):
        return max(self.leftToRight(s), self.rightToLeft(s))
    
    def leftToRight(self, string):
        left = 0
        right = 0
        totalcount = 0
        count = 0
        for i in string:
            if i == "(":
                left+=1
            else:
                right+=1
            if right > left:
                right = 0
                left = 0
            if right == left:
                count = left * 2
                totalcount= max(count, totalcount)
        return totalcount
    
    def rightToLeft(self, string):
        left = 0
        right = 0
        totalcount = 0
        count = 0
        for i in string[::-1]:
            if i == "(":
                left+=1
            else:
                right+=1
            if left > right:
                right = 0
                left = 0
            if right == left:
                count = right * 2
                totalcount= max(count, totalcount)
        return totalcount
    
    # (memory exceeded)
    def canJump(self, nums):
        n = len(nums)
        memo = set()
        def canJumpHelder(index):
            if index == n - 1:
                return True
            if index >= n:
                return False
            if index in memo:
                return False
            max_jump = index + nums[index]
            for next_index in range(index + 1, max_jump + 1):
                if canJumpHelder(next_index):
                    return True
            memo.add(index)
            return False
        return canJumpHelder(0)

    #optimal
    def canJump(self, nums):
        max_reach = 0
        
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True
    
    def climbStairs(self, n):
        memo = {}
        def helper(s, value):
            if s > n:
                return 0
            if s==n:
                return value + 1
            if s in memo:
                return memo[s]
            single = helper(s+1, value)
            double = helper(s+2, value)
            memo[s] = single+double
            return single+double
        return helper(0,0)