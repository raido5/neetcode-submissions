class Solution:
    def maxArea(self, heights: List[int]) -> int:

        contain=0



        l = 0
        r = len(heights)-1
        
        while r>l:

            contain = max(contain,min(heights[l],heights[r])*(r-l))

            if heights[r]>heights[l]:
                l+=1
            else: 
                r-=1
        return contain

            




