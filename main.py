from DynamicProgramming import DynamicProgramming

dyn = DynamicProgramming()

s = "()(()))))()(())"
# print(dyn.longestValidParentheses(s))

# arr = [[1,2,3],[4,5,6],[7,8,0]]
# target = [4,5,6]
# print(target in arr)
values = [2,1,0,1]
print(dyn.canJump(values))