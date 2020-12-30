'''
【计数排序】
遍历数组，找出最小值最大值
写出最小值到最大值之间的数，统计每个数出现的次数
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
当数值中有非整数时，计数数组的索引无法分配
时间复杂度O(n+k)
空间复杂度O(k)
稳定
'''


class Solution:
    def counting_sort(self, nums):
        if not nums:
            return []
        # 找到最小值和最大值
        min_num = min(nums)
        max_num = max(nums)
        # 计数列表
        count_list = [0] * (max_num - min_num + 1)
        # 计数
        for i in nums:
            count_list[i - min_num] += 1
        # 结果填到res中
        res = []
        for idx, i in enumerate(count_list):
            while i != 0:
                res.append(idx + min_num)
                i -= 1
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    nums5 = [2, 3, 4, 5, 2, 3, 4, 3, 2]
    print(u.counting_sort(nums1))
    print(u.counting_sort(nums2))
    print(u.counting_sort(nums3))
    print(u.counting_sort(nums4))
    print(u.counting_sort(nums5))
