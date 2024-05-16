class Solution:
    def minLength(self, s: str) -> int:
        stack  = [' ']
        for i in s[::-1]:
            if i+stack[-1]=="CD"or i+stack[-1]=="AB":
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        return len(stack)-1



        