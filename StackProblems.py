from OOPS.Stack.MyStack import MyStack
from collections import deque
import math

class StackProblems:

    def evalRPN(self, tokens):
        stack = []
        special_characters = ["+","/","*","-"]
        for i in tokens:
            if i == " ":
                continue
            if i in special_characters:
                rightOperand = int(stack.pop(-1))
                leftOperand = int(stack.pop(-1))
                stack.append(int(self.decideOperation(i, leftOperand, rightOperand)))
            else:
                stack.append(i)
        return stack[0]

    def decideOperation(self, operator, leftOperator, rightOperator):
        if operator == "+":
            return leftOperator+rightOperator
        if operator == "/":
            return leftOperator/rightOperator
        if operator == "*":
            return leftOperator*rightOperator
        else:
            return leftOperator-rightOperator
        
    
    def isValid(self, s):
        stack = deque()
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
                
            elif i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
    

    # time complexity O(3N) ~ O(N), Space complexity = O(N) use of stack.
    def simplifyPath(self, path):
        args = path.split("/")
        if path == "" or path == "/":
            return "/"

        stack = deque()
        for i in args:
            if i == "":
                continue
            elif i == ".":
                continue
            elif i == "..":
                if len(stack) > 0 :
                    stack.pop()
            else:
                stack.append(i)

        args = []    
        while(len(stack) > 0):
            args.append(stack.pop())


        return "/"+"/".join(args[::-1])
    
    # alternate solution given by GPT, works as well.

    def simplifyPath2(self, path: str) -> str:
        stack = deque()

        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)

    def removeComments(self, source):
        for i in source:
            print(i)
        return source

    def nextGreaterElement(self, nums1, nums2):
        nextGreatest = [-1]*len(nums2)

        monStack = deque()
        for i in range(len(nums2)):
            if len(monStack) == 0:
                monStack.append(i)
            else:
                if nums2[i] > nums2[monStack[-1]]:
                    while(len(monStack)>0 and nums2[i] > nums2[monStack[-1]]):
                        popped = monStack.pop()
                        nextGreatest[popped] = nums2[i]
                monStack.append(i)

        result = [-1]*len(nums1)
        for i in range(len(nums1)):
            result[i] = nextGreatest[nums2.index(nums1[i])]
        return result
    
    def nextGreaterElement(self, nums1, nums2):
        nge = {}
        stack = deque()

        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)

        while stack:
            nge[stack.pop()] = -1

        return [nge[num] for num in nums1]
    
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        monStack = deque()

        for i in range(len(temperatures)):
            if len(monStack) == 0:
                monStack.append(i)
            else:
                if temperatures[i] > temperatures[monStack[-1]]:
                    while(len(monStack)>0 and temperatures[i] > temperatures[monStack[-1]]):
                        popped = monStack.pop()
                        result[popped] = i
                monStack.append(i)

        for i in range(len(temperatures)):
            if result[i] != 0:
                result[i] = result[i] - i
        return result
    
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = deque()
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        return result
    
    def asteroidCollision(self, asteroids):
        stack = deque()

        for asteroid in asteroids:
            alive = True

            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                alive = False
                break

            if alive:
                stack.append(asteroid)

        return list(stack)

    
    def minAddToMakeValid(self, s):
        open = 0
        close = 0
        for i in s:
            if i == "(":
                open+=1
            else:
                if open > 0:
                    open-=1
                else:
                    close+=1
        return open+close
    
    def minInsertions(self, s):
        open = 0
        close = 0
        for i in s:
            if i == "(":
                open+=2
            else:
                if open == 0:
                    close+=1
                else:
                    open-=1
        if close % 2 == 0:
            close = close/2
        else:
            close = self.ceildiv(close,2)+1
        return open+close
    
    def ceildiv(self, a, b):
        return -(a // -b)
