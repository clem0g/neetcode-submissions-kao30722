class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        con = defaultdict(list)
        single_num = set(nums)
        ordered_num = sorted(single_num)
        num = list(ordered_num)
        if len(num) == 0:
            return 0
        else:
            j = 0 
            x = num[0] 
            for i in range(len(num)):
                if num[i] == x + 1:
                    con[j].append(num[i])
                    x = num[i]
                else:
                    j = j+ 1
                    con[j].append(num[i])
                    x = num[i]
            longest_con = max(con.values(), key = len) 
            z = len(longest_con) 
            return z



        