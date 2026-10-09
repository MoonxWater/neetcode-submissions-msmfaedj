class Solution:
    def calc(self, opr, left, right):
        match opr:
            case "+":
                return left + right
            case "-":
                return left - right
            case "*":
                return left * right
            case "/":
                return int(left / right)
            case _:
                return

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right, left = stack.pop(), stack.pop()
                res = self.calc(token, left, right)
                stack.append(res)

            else:
                stack.append(int(token))

        return stack[-1]