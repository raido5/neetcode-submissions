class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        prsum = [0]*len(nums)
        prsum[0]=nums[0]
        for i in range(1,len(nums)):
            prsum[i]=prsum[i-1]+nums[i]

        l=0
        r=0
        count = 100001
        while l<=r:
            somme = 0
            if l>0 : 
                somme = prsum[r]- prsum[l-1] 
            else: 
                somme = prsum[r]
            if somme<target:
                if r<len(prsum)-1:
                    r+=1
                else: 
                    l+=1
            else:
                count = min(count,r-l+1)
                l+=1

        if count == 100001: return 0
        return count

            

        