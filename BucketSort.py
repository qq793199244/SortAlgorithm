'''
【桶排序】
桶排序与计数排序类似，但可以解决非整数的排序
桶排序相当于把计数数组划分为按顺序的几个部分
每一部分叫做一个桶，它来存放处于该范围内的数
然后再对每个桶内部进行排序，可以使用其他排序方法如快速排序
最后整个桶数组就是排列好的数据，再将其返回给原序列
时间复杂度：平均O(n+k)，最好O(n+k)，最坏O(n^2)
空间复杂度：O(n+k)
稳定
'''
import math

class Solution:
    def bucket_sort(self, nums):
        n = len(nums)
        if n == 0:
            return []
        min_num = min(nums)
        max_num = max(nums)
        # 桶的大小
        bucket_size = math.ceil((max_num - min_num) / n)
        # 桶数组
        bucket_list = [[] for _ in range(n+1)]
        # 向桶数组填数
        for i in nums:
            bucket_list[(i - min_num) // bucket_size].append(i)
        res = []
        for bucket_nums in bucket_list:
            for num in sorted(bucket_nums):
                res.append(num)
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    nums5 = [2, 3, 4, 5, 2, 3, 4, 3, 2]
    print(u.bucket_sort(nums1))
    print(u.bucket_sort(nums2))
    print(u.bucket_sort(nums3))
    print(u.bucket_sort(nums4))
    print(u.bucket_sort(nums5))
