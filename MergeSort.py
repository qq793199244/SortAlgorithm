'''
【归并排序】
采用分治法，先将数组分成子序列，让子序列有序，再将子序列间有序，合并成有序数组。
算法描述：
①把长度为n的输入序列分成长度 n/2的子序列；
②对两个子序列采用归并排序；
③合并所有子序列。
时间复杂度O(nlogn)
空间复杂度O(n)
稳定，外排序
'''


class Solution:
    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        # 拆分
        mid = n // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        # 合并
        return self.merge(left, right)

    def merge(self, left, right):
        left_p, right_p = 0, 0
        res = []
        while left_p < len(left) and right_p < len(right):
            if left[left_p] <= right[right_p]:
                res.append(left[left_p])
                left_p += 1
            else:
                res.append(right[right_p])
                right_p += 1
        res += left[left_p:]
        res += right[right_p:]
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.merge_sort(nums1))
    print(u.merge_sort(nums2))
    print(u.merge_sort(nums3))
    print(u.merge_sort(nums4))
