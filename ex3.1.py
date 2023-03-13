#code from chatgpt
import sys


class Stack:
   def __init__(self):
       self.items = []
  
   def push(self, item):
       self.items.append(item)
  
   def pop(self):
       return self.items.pop()
  
   def is_empty(self):
       return len(self.items) == 0


def tokenize(expr):
   tokens = []
   current_token = ''
   for char in expr:
       if char == '(' or char == ')':
           if current_token != '':
               tokens.append(current_token)
               current_token = ''
           tokens.append(char)
       elif char == ' ':
           if current_token != '':
               tokens.append(current_token)
               current_token = ''
       else:
           current_token += char
   if current_token != '':
       tokens.append(current_token)
   return tokens


def shunting_yard(tokens):
   precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
   output = []
   operator_stack = []
   for token in tokens:
       if token.isdigit():
           output.append(token)
       elif token in ['+', '-', '*', '/']:
           while len(operator_stack) > 0 and operator_stack[-1] in ['+', '-', '*', '/'] and precedence[operator_stack[-1]] >= precedence[token]:
               output.append(operator_stack.pop())
           operator_stack.append(token)
       elif token == '(':
           operator_stack.append(token)
       elif token == ')':
           while len(operator_stack) > 0 and operator_stack[-1] != '(':
               output.append(operator_stack.pop())
           if len(operator_stack) > 0 and operator_stack[-1] == '(':
               operator_stack.pop()
   while len(operator_stack) > 0:
       output.append(operator_stack.pop())
   return output


def evaluate(expr):
   stack = Stack()


   tokens = tokenize(expr)
   postfix_tokens = shunting_yard(tokens)
   for token in postfix_tokens:
       if token.isdigit():
           stack.push(int(token))
       elif token in ['+', '-', '*', '/']:
           arg2 = stack.pop()
           arg1 = stack.pop()
           if token == '+':
               stack.push(arg1 + arg2)
           elif token == '-':
               stack.push(arg1 - arg2)
           elif token == '*':
               stack.push(arg1 * arg2)
           elif token == '/':
               stack.push(arg1 / arg2)


   return stack.pop()




expression = sys.argv[1]
result = evaluate(expression)
print(int(result))



