class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            rl, rm, ll, lm = 0, 0, 0, 0
            for j in range(i+1, len(rating)):
                if rating[j]<rating[i]:
                    rl+=1
                elif rating[j]>rating[i]:
                    rm+=1
            for j in range(i):
                if rating[j]<rating[i]:
                    ll+=1
                elif rating[j]>rating[i]:
                    lm+=1
            count += rl*lm + rm*ll
        return count
        

        
