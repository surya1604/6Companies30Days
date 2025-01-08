class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        secretList=[0]*10

        for s,g in zip(secret,guess):
            if s==g:
                bulls+=1
            else:
                secretList[int(s)]+=1
                secretList[int(g)]-=1
        return f'{bulls}A{len(secret)-bulls-sum(x for x in secretList if x>0)}B'
        
