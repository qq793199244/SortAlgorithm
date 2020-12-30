'''
【快速排序】
基本思想：
1．先从数列中取出一个数作为基准数pivot。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3. 以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩一个元素为止。

快排的时间复杂度受到所选择数字的影响，最坏的情况是每次找到的数字x均为最大或者最小，
使得划分后一侧有n-1个数字，这样是时间复杂度为n^2，
如果每次找的数字x都为中值，那么时间复杂度nlogn，这是最好的情况，快速排序的平均时间复杂度可以证明为 nlogn

时间复杂度：平均O(nlogn)，最好O(nlogn)，最坏O(n^2)
空间复杂度：O(logn)~O(n)
不稳定
'''


class Solution:

    # 递归版本
    def quick_sort(self, nums, start, end):
        if not nums:
            return []
        if start >= end:
            return
        pivot = nums[start]
        low, high = start, end
        while low < high:
            # high左移
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] < pivot:
                low += 1
            nums[high] = nums[low]
        # 从while循环退出时，low和high相等
        nums[low] = pivot

        # 对low左边的列表进行快速排序
        self.quick_sort(nums, start, low-1)
        # 对low右边的列表进行快速排序
        self.quick_sort(nums, low+1, end)
        return nums

    # 非递归版本
    '''
    递归调用是一个重复自身的过程，可以在程序中模拟一个堆栈，
    然后再使用for循环或者while循环完成其重复调用的部分，
    就可以将递归调用的算法，转换成非递归的实现。
    '''
    def quick_sort2(self, nums):
        pass


if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.quick_sort(nums1, 0, len(nums1)-1))
    print(u.quick_sort(nums2, 0, len(nums2)-1))
    print(u.quick_sort(nums3, 0, len(nums3)-1))
    print(u.quick_sort(nums4, 0, len(nums4)-1))
