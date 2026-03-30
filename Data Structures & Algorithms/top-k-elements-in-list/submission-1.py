class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = defaultdict(int)
        for i in nums:
            numDict[i] += 1
        freq_list = []
        for num, freq in numDict.items():
            freq_list.append((num, freq))
            
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
            
        return result


                
            