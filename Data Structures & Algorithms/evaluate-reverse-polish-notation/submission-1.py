import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        strToOp = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)  # ensure truncation toward 0
        }

        for token in tokens:
            if token in strToOp:
                r = stack.pop()
                l = stack.pop()
                op = strToOp[token]
                stack.append(op(l, r))
            else:
                stack.append(int(token))

        return stack[0]