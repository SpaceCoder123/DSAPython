def evalRPN(tokens):
    stack = []
    special_characters = ["+","/","*","-"]
    for i in tokens:
        if i == " ":
            continue
        if i in special_characters:
            rightOperand = int(stack.pop(-1))
            leftOperand = int(stack.pop(-1))
            stack.append(int(decideOperation(i, leftOperand, rightOperand)))
        else:
            stack.append(i)
    return stack[0]

def decideOperation(operator, leftOperator, rightOperator):
    if operator == "+":
        return leftOperator+rightOperator
    if operator == "/":
        return leftOperator/rightOperator
    if operator == "*":
        return leftOperator*rightOperator
    else:
        return leftOperator-rightOperator

token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(token))
