class Solution:
    def checkValidString(self, s: str) -> bool:
        pStack = []
        sStack = []

        for i in range(len(s)):
            if s[i] == "(":
                pStack.append(i)
            elif s[i] == "*":
                sStack.append(i)
            else:
                if pStack: 
                    pStack.pop()
                elif sStack:
                    sStack.pop()
                else:
                    return False
        
        while pStack:
            if not sStack or pStack.pop() > sStack.pop():
                return False
        

        return True