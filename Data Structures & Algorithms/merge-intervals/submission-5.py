class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals)==1): return intervals

        intervals.sort()
        final=[]
        final.append(intervals[0])

        j=0
        for i in range(1,len(intervals)):
            inter1=final[j]
            inter2=intervals[i]

            if inter2[0]<=inter1[1]:
                final[j][1]=max(inter1[1],inter2[1])
            else:
                final.append(inter2)
                j+=1
        return final