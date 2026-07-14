class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area ,  height * width)

            stack.append(i)

        #flush remaining bars
        while stack:
                height = heights[stack.pop()]
                if not stack:
                    width = len(heights)
                else:
                    width = len(heights) - stack[-1] - 1

                max_area = max(max_area ,  height * width)


        return max_area

        