class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if stack and mapping[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack