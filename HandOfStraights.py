# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        trial = Counter(hand)
        sorted_keys = sorted(trial.keys())
        for key in sorted_keys:
            if trial[key]>0:
                count = trial[key]
                for i in range(key, key+groupSize):
                    if trial[i]<count:
                        return False
                    trial[i]-=count
        return True
