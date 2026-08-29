class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = {}
        count = [[]for i in range(len(nums)+1)]

        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        for kk,v in freq.items():
            count[v].append(kk)

        f = []

        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                f.append(num)

                if len(f) == k:
                    return f

