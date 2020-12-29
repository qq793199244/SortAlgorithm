'''
【选择排序】
找到最小的元素，放到已排序序列末尾
时间复杂度O(n^2)
空间复杂度O(1)
不稳定
'''


class Solution:
    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            min_num_idx = i
            for j in range(i, n):
                if nums[j] < nums[min_num_idx]:
                    min_num_idx = j
            nums[i], nums[min_num_idx] = nums[min_num_idx], nums[i]
        return nums


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.selection_sort(nums1))
    print(u.selection_sort(nums2))
    print(u.selection_sort(nums3))
    print(u.selection_sort(nums4))
