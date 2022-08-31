class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull=0
        cows=0
        s=Counter(secret)
        visited=set()
     
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                s[guess[i]]-=1
                visited.add(i)
        for i in range(len(secret)):
            if i not in visited and guess[i] in s and s[guess[i]]>0:
                s[guess[i]]-=1
                cows+=1
        return str(bull)+"A"+str(cows)+"B"
        