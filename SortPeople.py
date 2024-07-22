# Return names sorted in descending order by the people's heights.
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict = {}
        for i in range(len(names)):
            my_dict[heights[i]]=names[i]
        heights.sort(reverse=True)
        return [my_dict[i] for i in heights]
        
