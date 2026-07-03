class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operations:
                a = stack.pop()
                b = stack.pop()
                c = eval(f'{b} {token} {a}')
                stack.append(int(c))
                print(a, b, c, token, stack)
            else:
                stack.append(token)

        return int(stack[0])