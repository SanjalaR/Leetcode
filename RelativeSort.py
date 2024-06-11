# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        end = [i for i in arr1 if i not in arr2]
        end.sort()
        arr1 = [i for i in arr1 if i in arr2]
        hash_ = Counter(arr1)
        arr1 = []
        for i in arr2:
            arr1.extend([i]*(hash_[i]))
        arr1.extend(end)
        return arr1
