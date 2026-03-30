class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for i in range(len(strs)):
            if len(strs) == 1:
                output.append([])
                output[-1].append(strs[i])
            elif any(strs[i] in sublist for sublist in output) == False:
                output.append([])
                output[-1].append(strs[i])
                for j in range(i + 1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        output[-1].append(strs[j])
            else:
                pass
        return output
                