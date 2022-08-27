class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        
        arr=[[False]*(len(s)+1) for i in range(len(p)+1)]
        arr[-1][-1]=True
        
        for row in range(len(p)-1,-1,-1):
            if p[row]=='*':
                arr[row][-1]=arr[row+1][-1]
            
        for row in range(len(p)-1,-1,-1):
            for col in range(len(s)-1,-1,-1):
                if p[row]=='*':
                    arr[row][col]= arr[row+1][col] or arr[row][col+1]
                elif (p[row]==s[col] or p[row]=='?'):
                    arr[row][col]=arr[row+1][col+1]
     
        return arr[0][0]
                
                    
                
                
                
            
        