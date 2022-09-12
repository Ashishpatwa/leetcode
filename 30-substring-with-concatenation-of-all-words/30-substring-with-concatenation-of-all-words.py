class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq=dict()
        for i in words:
            freq[i]=freq.get(i,0)+1
        c=len(words)*len(words[0])
        ans=[]
        i=0
        while i<len(s)-c+1:
            flag=1
            freqs=freq.copy()
            j=i
            while j<i+c:
                k=s[j:j+len(words[0])]
                if k in freqs and freqs[k]:
                    freqs[k]-=1
                    j+=len(words[0])
                else:
                    flag=0
                    break
            if flag:
                ans.append(i)
            
            i+=1
        return ans
            
            
        