class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        have,check = {},{}
        for i in t:
            check[i] = 1 + check.get(i, 0)

        h, c = 0, len(check)
        res, resLen = [-1,-1], float("infinity")
        # x,y = 1000,1000
        l = 0

        for r in range(len(s)):
            x = s[r]
            have[x] = 1 + have.get(x, 0)

            if x in check and have[x] == check[x]:

                h +=1

            while h == c:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                have[s[l]] -=1
                    # x = min(l,x)
                    # y = min(j,y)
                if s[l] in check and have[s[l]] < check[s[l]]:
                    h -= 1
                l +=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""





