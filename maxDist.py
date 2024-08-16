class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn = arrays[0][0]
        maxx = arrays[0][-1]
        dist=0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            dist = max(dist, abs(arr[-1] - minn), abs(maxx - arr[0]))
            minn = min(minn, arr[0])
            maxx = max(maxx, arr[-1])
        return dist
