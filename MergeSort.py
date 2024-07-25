# Sort an array in nlogn time complexity
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, left, mid, right):
            left_arr = nums[left:mid+1]
            right_arr = nums[mid+1:right+1]
            i = j = 0
            k = left
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    nums[k] = left_arr[i]
                    i += 1
                else:
                    nums[k] = right_arr[j]
                    j += 1
                k += 1
            while i < len(left_arr):
                nums[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                nums[k] = right_arr[j]
                j += 1
                k += 1

        def merge_sort(nums, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(nums, left, mid)
                merge_sort(nums, mid + 1, right)
                merge(nums, left, mid, right)

        merge_sort(nums, 0, len(nums) - 1)
        return nums
