'''
【快速排序】
基本思想：
1．先从数列中取出一个数作为基准数pivot。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3. 以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩一个元素为止。
时间复杂度O(nlogn)
空间复杂度O(1)
不稳定
'''


class Solution:

    # 递归版本
    def quick_sort(self, nums):
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j - 1)
            quick(j + 1, right)
            return nums

        return quick(0, n - 1)


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.quick_sort(nums1))
    print(u.quick_sort(nums2))
    print(u.quick_sort(nums3))
    print(u.quick_sort(nums4))
