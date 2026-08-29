class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ss = set()
        for i in nums:
            ss.add(i)


        maxx= 0
        for i in nums:
            count=0
            if i-1 not in ss:
                j=i
                count+=1
                while j+1 in ss:
                    count+=1
                    j+=1
                maxx=max(maxx,count)
                count =0
        return maxx

        
        