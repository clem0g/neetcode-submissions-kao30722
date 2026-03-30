class Solution:
    def isValid(self, s: str) -> bool:
        # We use a stack to keep track of opening brackets
        stack = []
        # Mapping closing brackets to their opening counterparts
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in pairs:
                # If we see a closer, check the top of the stack
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # If we see an opener, push it onto the stack
                stack.append(char)

        # If the stack is empty, every opener found its match in the right order
        return not stack
            

            
        