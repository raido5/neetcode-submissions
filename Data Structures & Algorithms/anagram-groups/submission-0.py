class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        m = {}
        for i in strs:
            l = [0]*26
            for f in i:
                l[ord(f)-ord('a')]+=1
            
            ss = m.get(tuple(l),[])
            ss.append(i)
            m[tuple(l)]= ss

        ll = []
        for i in m:
            ll.append(m.get(i))
        return ll
        


        