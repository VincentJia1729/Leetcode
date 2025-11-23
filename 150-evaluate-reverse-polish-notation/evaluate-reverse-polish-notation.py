class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                a,b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif c == "-":
                a,b = stack.pop(), stack.pop() 
                # a is top of stack
                # b is second top on stack
                # the way "-" works in Reverse Polish Notation is if we have 1, 2, "-"
                # then we do 1-2 = -1 
                # this is b, a, "-". This is b-a
                stack.append(b-a)
                
            elif c == "*":
                a,b = stack.pop(), stack.pop() 
                stack.append(a*b)
                
            elif c == "/":
                # a is top of stack
                # b is second top on stack
                # the way "/" works in Reverse Polish Notation is if we have 1, 2, "/"
                # then we do 1/2 = 0. This is because we round toward 0 and do integer division
                a,b = stack.pop(), stack.pop() 
                stack.append(int(b/a))
                
            else:
                stack.append(int(c))

        return stack[0]
        