'''
【希尔排序】
一种高效的插入排序
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。

时间复杂度O(nlogn)
空间复杂度O(1)
不稳定
'''
class Solution:
    def shell_sort(self, nums):
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i >= gap and nums[i-gap] > nums[i]:
                    nums[i-gap], nums[i] = nums[i], nums[i-gap]
                    i -= gap
            gap //= 2
        return nums


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.shell_sort(nums1))
    print(u.shell_sort(nums2))
    print(u.shell_sort(nums3))
    print(u.shell_sort(nums4))