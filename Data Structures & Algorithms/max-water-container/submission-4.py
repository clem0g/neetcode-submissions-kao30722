class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x = max(heights)
        max_height = 123
        for i in range(len(heights)):
            if heights[i] == x and heights[i] != max_height:
                max_height = heights[i]
                max_i = i
                break
        l,r = 0, max_i + 1
        l_max = 0
        r_max = 0
        t_max = 0
        m_len = 0
        len_curr = 0
        r_end = len(heights)-1
        max_length = len(heights) - 1
        while max_length >= max_i:
            if heights[l] <= heights[r_end]:
                len_curr = heights[l] * max_length
                m_len = max(m_len, len_curr)
                if l < r_end:
                    l += 1
                    max_length -= 1
                else:
                    break
            else:
                len_curr = heights[r_end] * max_length
                m_len = max(m_len, len_curr)
                if l < r_end:
                    r_end -= 1
                    max_length -= 1
                else:
                    break
        while l < max_i:
            l_length = max_i - l
            left_curr = heights[l] * l_length
            l_max = max(l_max, left_curr)
            if l < max_i:
                l+=1
        while r < len(heights):      
            r_length = r - max_i
            right_curr = heights[r] * r_length
            r_max = max(r_max,right_curr)
            if r < len(heights):
                r+=1
        t_max = max(r_max,l_max, m_len)
        return t_max


            