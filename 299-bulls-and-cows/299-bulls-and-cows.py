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
        visited=[False]*len(secret)
     
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                s[guess[i]]-=1
                visited[i]=True
        for i in range(len(secret)):
            if guess[i] in s and s[guess[i]]>0 and visited[i]==False:
                s[guess[i]]-=1
                cows+=1
        return str(bull)+"A"+str(cows)+"B"
        