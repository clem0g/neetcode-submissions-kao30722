class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.replace(" ","")
        y = x.lower()
        l = 0
        r = len(y) -1
        while l < r:
            if not y[l].isalnum():
                l +=1
            if not y[r].isalnum():
                r-=1
            if y[l].isalnum() and y[r].isalnum():
                if y[l] != y[r]:
                    return [y[l],y[r]]
            l += 1
            r -= 1
        return True
        