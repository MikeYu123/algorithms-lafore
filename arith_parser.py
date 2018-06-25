from queues.array_stack import ArrayStack
import re
# TODO rework so it takes more than single-digit numbers
class ArithParser:
    def in_to_post(self, input):
        output = ''
        stack = ArrayStack(100)
        for char in input:
            if re.match('[A-Za-z0-9]', char):
                output += char
            elif char == '(':
                stack.push(char)
            elif re.match('[/*+-]', char):
                while not stack.isEmpty():
                    op = stack.pop()
                    if op == '(':
                        stack.push(op)
                        break
                    elif (op in ['-', '+'] and char in ['*', '/']):
                        stack.push(op)
                        break
                    else:
                        output += op
                stack.push(char)
            elif char == ')':
                while not stack.isEmpty():
                    op = stack.pop()
                    if op == '(':
                        break
                    else:
                        output += op
        while not stack.isEmpty():
            output+=stack.pop()
        return output

    def post_to_result(self, input):
        output = 0
        stack = ArrayStack(100)
        for char in input:
            if char == '+':
                stack.push(stack.pop() + stack.pop())
            elif char == '-':
                first, second = stack.pop(), stack.pop()
                stack.push(second - first)
            elif char == '/':
                first, second = stack.pop(), stack.pop()
                stack.push(second / first)
            elif char == '*':
                stack.push(stack.pop() * stack.pop())
            elif re.match('\d', char):
                stack.push(int(char))
        return stack.pop()

    def parse(self, input):
        return self.post_to_result(self.in_to_post(input))
