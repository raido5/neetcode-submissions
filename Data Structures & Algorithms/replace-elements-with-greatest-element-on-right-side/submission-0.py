class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        arrr = arr
        maxx = arrr[-1]
        
        for i in range(len(arrr)-1,-1,-1):
            temp = arrr[i]
            arrr[i]=maxx
            maxx = max(temp,maxx)
            
        
        arrr[-1]=-1

        return arrr