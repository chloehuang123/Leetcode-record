class Solution:
    def isValid(self, s: str) -> bool:
        hashTb = {']' : '[', ')' : '(', '}' : '{'}
        stack = []

        for element in s:
            if element in hashTb:
                if stack and stack[-1] == hashTb[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        return True if not stack else False
