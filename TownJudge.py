# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1 if not trust else -1
            
        mem1 = set()
        mem2 = set()

        for i in trust:
            mem1.add(i[0])
            mem2.add(i[1])

        potential_judges = mem2 - mem1

        if len(potential_judges) != 1:
            return -1

        judge = potential_judges.pop()

        for i in range(1, n + 1):
            if i != judge and [i, judge] not in trust:
                return -1

        return judge
