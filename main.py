from DynamicProgramming import DynamicProgramming
from Recursion import RecursionProblems

dyn = DynamicProgramming()

s = "()(()))))()(())"
# print(dyn.longestValidParentheses(s))

# arr = [[1,2,3],[4,5,6],[7,8,0]]
# target = [4,5,6]
# print(target in arr)
# values = [2,1,0,1]
# print(dyn.canJump(values))

rec = RecursionProblems()
# L = [1,2,2]
n= 3
k= 7
# print(rec.subsets(L))
print(rec.combinationSum(n,k))