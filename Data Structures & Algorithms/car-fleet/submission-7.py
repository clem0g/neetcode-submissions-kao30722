class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d_position = sorted(position)
        o_position = list(d_position)
        stack =[]
        stuff ={}
        for i in range(len(position)):
            stuff[position[i]] = speed[i]
        for t in range(len(o_position)-1,-1, -1):
            time = (target - o_position[t]) / stuff[o_position[t]]
            if t == len(o_position)-1 :
                stack.append(time)
            elif stack and time <= stack[-1]:
                pass
            elif stack and time > stack[-1]:
                stack[-1] = time
                stack.append(time)
        return len(stack)

            

