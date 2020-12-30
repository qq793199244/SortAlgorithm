'''
【堆排序】
算法描述：
①建堆，从底向上调整堆，使得父亲节点比孩子节点值大，构成大顶堆；
②交换堆顶和最后一个元素，重新调整堆。
时间复杂度O(nlogn)
空间复杂度O(1)
不稳定
'''
class Solution:
    def heap_sort(self, nums):
        def adjust_heap(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                adjust_heap(nums, n, largest)
        # 建堆
        n = len(nums)
        for i in range(n, -1, -1):
            adjust_heap(nums, n, i)

        # 一个个交换元素
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            adjust_heap(nums, i, 0)
        return nums



if __name__ == '__main__':
    u = Solution()
    nums1 = [8, 5, 3, 1, 7, 2, 6]
    nums2 = [7, 6, 5, 4, 3, 2, 1]
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    nums4 = []
    print(u.heap_sort(nums1))
    print(u.heap_sort(nums2))
    print(u.heap_sort(nums3))
    print(u.heap_sort(nums4))