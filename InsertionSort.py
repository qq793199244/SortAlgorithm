'''
【插入排序】
通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
时间复杂度O(n^2)
空间复杂度O(1)
稳定
'''


class Solution:
    def insertion_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
            # print('本次排序：', nums)
        return nums


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.insertion_sort(nums1))
    print(u.insertion_sort(nums2))
    print(u.insertion_sort(nums3))
    print(u.insertion_sort(nums4))
