class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Each element is (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i  # This marks where the rectangle of height `h` could potentially start

            # Pop all bars that are taller than the current one,
            # because the current bar sets a right boundary for them
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                # The width of the rectangle is from that index to the current index
                width = i - index
                max_area = max(max_area, height * width)
                start = index  # Update `start` to the leftmost position of popped bar

            # Push current bar with the correct start position
            stack.append((start, h))

        # Final pass: resolve any bars still in the stack
        # All these bars extend to the end of the histogram
        for i, h in stack:
            width = len(heights) - i
            max_area = max(max_area, h * width)

        return max_area
