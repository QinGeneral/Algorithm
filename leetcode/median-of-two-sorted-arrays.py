class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1
            else:
                merge.append(nums1[i])
                i += 1
        if i < len(nums1):
            for j in range(i, len(nums1)):
                merge.append(nums1[j])
        if j < len(nums2):
            for i in range(j, len(nums2)):
                merge.append(nums2[i])
        print(merge)
        mid = (len(merge) - 1) // 2
        if len(merge) % 2 == 0:
            return (merge[mid] + merge[mid + 1]) / 2
        else:
            return merge[mid]
