class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                item1 = stack.pop()
                item2 = stack.pop()
                if i == "/":
                    result = int(item2 / item1)

                else:
                    expr= f"{item2}{i}{item1}"
                    result = eval(expr)
                stack.append(result)

        return int(stack[-1])