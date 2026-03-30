class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new = []
        for i in range(len(numbers)):
            for j in range (i +1 , len(numbers)):
                if numbers[i] + numbers[j] == target:
                    new.append(i + 1)
                    new.append(j + 1)
                    return new