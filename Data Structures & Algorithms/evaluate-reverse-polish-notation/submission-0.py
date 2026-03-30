# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         x = 0
#         for i in range(len(tokens)):
#             if stack and (stack[-1] =='+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] =='/'):
#                 if stack[-1] == '+':
#                     x = int(stack[0]) + int(stack[1])
#                 if stack[-1] == '*':
#                     x = int(stack[0]) * int(stack[1])
#                 if stack[-1] == '-':
#                     x = int(stack[0]) - int(stack[1])
#                 if stack[-1] == '/':
#                     x = int(stack[0]) / int(stack[1])
#                 stack=[]
#                 stack.append(x)
#             stack.append(tokens[i])
#         return int(stack[0])
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])
