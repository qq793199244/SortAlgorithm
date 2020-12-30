'''
【基数排序】
第一类：最低位优先法，简称LSD法：先从最低位开始排序，再对次低位排序，直到对最高位排序后得到一个有序序列；
第二类：最高位优先法，简称MSD法：先从最高位开始排序，再逐个对各分组按次高位进行子排序，循环直到最低位。（位没有数的话，补0）
这里以LSD为例，由于待排序元素每一位上的数字的取值范围是0—9，因此每按照某一位，需要10个桶，这样每一位上相同的数字会分配到一个桶里。
时间复杂度O(nk)
空间复杂度O(n+k)
稳定
'''


class Solution:
    def radix_sort(self, nums):
        if not nums:
            return []
        max_num = max(nums)
        place = 1
        # 找最高几位
        while max_num >= 10 ** place:
            place += 1
        for i in range(place):
            # 0~9 十个桶
            buckets = [[] for _ in range(10)]
            for num in nums:
                radix = int(num / (10 ** i) % 10)
                buckets[radix].append(num)
            # j 表示合并桶中的数据时，将数据赋值给待排序列表中索引 j 的位置。
            j = 0
            for k in range(10):
                for num in buckets[k]:
                    nums[j] = num
                    j += 1
        return nums


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    nums5 = [12, 34, 54, 332, 676, 43, 32, 76]
    print(u.radix_sort(nums1))
    print(u.radix_sort(nums2))
    print(u.radix_sort(nums3))
    print(u.radix_sort(nums4))
    print(u.radix_sort(nums5))
