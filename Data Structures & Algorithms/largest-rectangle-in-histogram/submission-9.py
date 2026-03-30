class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0
        for i in range(len(heights)):
            if i == 0:
                stack.append(heights[i])
            else:
                if heights[i] == 0:
                    A = len(stack) * min(stack)
                    maxA = max(maxA, A)
                    stack = []
                    stack.append(heights[i]) 
                else: 
                    if stack and heights[i] <= stack[-1]:
                        stack.append(heights[i])
                        A = len(stack) * min(stack)
                        maxA = max(maxA, A)
                    elif heights[i] > stack[-1]:
                        l = i
                        while l < len(heights):
                            stack.append(heights[l])
                            A = len(stack) * min(stack)
                            maxA = max(maxA, A)
                            l+=1
                        stack = []
                        stack.append(heights[i])
        A = len(stack) * min(stack)
        maxA = max(maxA, A)
        return maxA

