class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operations:
                a = stack.pop()
                b = stack.pop()
                token = int(eval(f'{b} {token} {a}'))
                print(token)
            stack.append(token)
        return int(stack[0])