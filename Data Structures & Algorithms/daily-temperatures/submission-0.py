class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        res = [0]*len(temperatures)
        stack.append((temperatures[0],0))
        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i],i))

            
        return res