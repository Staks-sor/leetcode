class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            max_of_left = max(nums1[i-1] if i > 0 else float('-inf'), nums2[j-1] if j > 0 else float('-inf'))
            min_of_right = min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))
            
            if max_of_left <= min_of_right:
                if (m + n) % 2 == 1:
                    return max_of_left
                else:
                    return (max_of_left + min_of_right) / 2.0
                
            elif nums2[j-1] > nums1[i]:
                imin = i + 1
            else:
                imax = i - 1
