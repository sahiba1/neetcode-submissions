class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid =(left+right)//2
            if nums[mid] == target:
                return mid 
            elif nums[left] <= nums[mid]:
                #left is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1     # search left half
                else:
                    left = mid + 1      # search right half
            elif nums[left] > nums[mid]:
                #right is sorted

                if nums[right] >= target > nums[mid]:
                    left = mid + 1     # search left half
                else:
                    right = mid - 1 

        return -1


        