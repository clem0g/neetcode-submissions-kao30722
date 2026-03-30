class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {'}' :'{',')': '(',']': '['}
        for i in s:
            if i in key:
                if not stack or stack.pop() != key[i]:
                    return False
            else:
                stack.append(i)
        return not stack
            

            
        