class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for i in range(len(tokens)):
            if not tokens[i] in "+-*/":
                stk.append(int(tokens[i]))
            else:
                if stk:
                    if tokens[i] == '+':
                        stk[-2] += stk[-1]
                    elif tokens[i] == '-':
                        stk[-2] -= stk[-1]
                    elif tokens[i] == '*':
                        stk[-2] *= stk[-1]
                    else:
                        stk[-2] = int(stk[-2] / stk[-1])
                    stk.pop()
        return stk[0]