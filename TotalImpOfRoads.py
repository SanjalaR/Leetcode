# Return the maximum total importance of all roads possible after assigning the values optimally.
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        my_dict = {}
        for i in range(n):
            my_dict[i]=0
        for i in roads:
            my_dict[i[0]]+=1
            my_dict[i[1]]+=1
        sorted_dict = dict(zip(sorted(my_dict, key=my_dict.get,
                               reverse=True), reversed(sorted(my_dict.values()))))
        print(sorted_dict)
        cities = []
        for key in sorted_dict.keys():
            cities.append(key)
        print(cities)
        total_imp = 0
        for i in range(n):
            total_imp += (n-i)*sorted_dict[cities[i]]
        return total_imp
