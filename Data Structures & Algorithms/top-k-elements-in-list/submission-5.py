class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        res =[]
        max_n = 0
        for i in nums:
            numbers[i] = 1 + numbers.get(i,0)

        for i in range(k):
            top = max(numbers, key = numbers.get)
            res.append(top)
            del numbers[top]
        
        return res

            
