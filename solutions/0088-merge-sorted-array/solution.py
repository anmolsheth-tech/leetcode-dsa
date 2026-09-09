class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #m and n are no.of numbers in num1 & num2 respectively
        #The important trick is that you should merge from the right side, because the empty spaces are at the end of nums1
        #i = pointing to the last actual element in nums1
        #j = One pointing to the last element in nums2
        #k = pointing to the last position of the final merged array
        #at every step, compare nums1[i] to nums2[j], whichever is larger, goes to nums1[k], and whichever is larger , that poointer moves backwards
        #Whichever number you take → move that array's pointer.
        #And always move k.
        #if an array runs out, Only remaining elements from nums2 need to be copied.
        #3 pointers approach
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
