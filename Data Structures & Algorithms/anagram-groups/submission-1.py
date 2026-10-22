class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            sorted_s = "".join(sorted(strs[i]))
            res[sorted_s].append(strs[i])
        return list(res.values())

