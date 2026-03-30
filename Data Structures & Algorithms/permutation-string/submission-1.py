class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        check = sorted(s1)
        lookup = []
        l = 0
        for r in range(len(s2)):
            while (r - l) == k:
                lookup.remove(s2[l])
                l +=1
            lookup.append(s2[r])
            
            if sorted(lookup) == check:
                return True
        return False

        