class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = []
        for i in range(len(temperatures)):
            r = i
            stack.append(temperatures[i])
            if temperatures[i] >= stack[-1]:
                while r < len(temperatures)-1 and temperatures[i] >= stack[-1]:
                    stack.pop()
                    stack.append(temperatures[r+1])
                    r+=1
                if temperatures[i] < stack[-1]:
                    output.append(r - i)
                else:
                    output.append(0) 
        return output