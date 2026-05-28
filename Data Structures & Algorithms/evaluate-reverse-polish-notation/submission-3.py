class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            '+': lambda a,b: a + b,
            '-': lambda a,b: a - b,
            '*': lambda a,b: a * b,
            '/': lambda a,b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token in operands:
                b, a = stack.pop(), stack.pop()
                result = operands[token](int(a),int(b))
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]
        