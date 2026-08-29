class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s = {}

        for i in range(0,len(nums)):
            s[nums[i]]=i

        l = []
        for i in range(0,len(nums)):
            if (s.get(target-nums[i],-1)!=-1 and s.get(target-nums[i],-1)!=i):
                l.append(i)
                l.append(s.get(target-nums[i]))
                break
        return l
            


            
