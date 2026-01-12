from OOPS.Stack.MyStack import MyStack
from collections import deque
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