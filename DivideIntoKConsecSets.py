# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        trial = Counter(nums)
        sorted_keys = sorted(trial.keys())
        for key in sorted_keys:
            if trial[key]>0:
                count = trial[key]
                for i in range(key, key+k):
                    if trial[i]<count:
                        return False
                    trial[i]-=count
        return True
