class Solution:
    def checkValidString(self, s: str) -> bool:
        leftParenthesisStack = []
        starStack = []

        for k, i in enumerate(s):
            if i == "(":
                leftParenthesisStack.append(k)
            elif i == "*":
                starStack.append(k)
            elif i == ")":
                if len(leftParenthesisStack) > 0:
                    leftParenthesisStack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
                else:
                    return False
        
        if len(leftParenthesisStack) == 0:
            return True
        
        while leftParenthesisStack:
            if len(starStack) == 0 or leftParenthesisStack.pop() > starStack.pop():
                return False
        
        return True