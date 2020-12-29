'''
【冒泡排序】
比较相邻元素，大的元素后置。
时间复杂度O(n^2)
空间复杂度O(1)
稳定
'''


class Solution:
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(1, n):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.bubble_sort(nums1))
    print(u.bubble_sort(nums2))
    print(u.bubble_sort(nums3))
    print(u.bubble_sort(nums4))
