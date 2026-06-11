class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        # Always binary search the SMALLER array.
        # This keeps our search space O(log(min(m,n)))
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)

        # Total number of elements
        total = m + n

        # Number of elements that should be on the LEFT side
        #
        # Examples:
        #
        # total = 8
        # left side should contain 4
        #
        # total = 7
        # left side should contain 4
        #
        # The +1 handles odd lengths nicely.
        half = (total + 1) // 2

        # Binary search over possible partition positions in A
        #
        # Example:
        #
        # A = [1,3,8]
        #
        # possible cuts:
        #
        # |1,3,8
        # 1|3,8
        # 1,3|8
        # 1,3,8|
        #
        l, r = 0, m

        while l <= r:

            # Partition index in A
            i = (l + r) // 2

            # Partition index in B
            #
            # Together they must contribute exactly
            # "half" elements to the left side.
            j = half - i

            # --------------------------
            # Border values around cut
            # --------------------------

            # Largest value on left side of A
            #
            # If cut is all the way left,
            # there is no left value.
            #
            # Use -infinity so comparisons work.
            Aleft = A[i - 1] if i > 0 else float("-inf")

            # Smallest value on right side of A
            #
            # If cut is all the way right,
            # there is no right value.
            #
            # Use +infinity so comparisons work.
            Aright = A[i] if i < m else float("inf")

            # Same idea for B
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # -------------------------------------------------
            # Check whether partition is valid
            #
            # We need:
            #
            # every left value <= every right value
            #
            # Since arrays are sorted,
            # we only need to compare the borders.
            # -------------------------------------------------
            if Aleft <= Bright and Bleft <= Aright:

                # -------------------------
                # Odd total length
                # -------------------------
                #
                # Example:
                #
                # [1,2,3,4 | 5,6,7]
                #
                # Median is largest value
                # on left side.
                #
                if total % 2:
                    return max(Aleft, Bleft)

                # -------------------------
                # Even total length
                # -------------------------
                #
                # Example:
                #
                # [1,2,3,4 | 5,6,7,8]
                #
                # Median = average of
                # largest left and smallest right
                #
                return (
                    max(Aleft, Bleft)
                    + min(Aright, Bright)
                ) / 2

            # -------------------------------------------------
            # Too many elements taken from A
            # -------------------------------------------------
            #
            # Example:
            #
            # Aleft = 8
            # Bright = 4
            #
            # 8 should be on the right side.
            #
            # Move partition LEFT.
            #
            elif Aleft > Bright:
                r = i - 1

            # -------------------------------------------------
            # Too few elements taken from A
            # -------------------------------------------------
            #
            # Example:
            #
            # Bleft = 7
            # Aright = 3
            #
            # Need more values from A on left side.
            #
            # Move partition RIGHT.
            #
            else:
                l = i + 1