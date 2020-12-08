class Solution:
    def spiralOrder(self, matrix: list[[int]]) -> list[int]:

        result = []
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while True:
            # 从左到右
            for i in range(left, right+1):
                result.append(matrix[top][i])
            # 往下走
            top += 1
            if top > bottom:
                break

            # 从上到下
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            # 往左走
            right -= 1
            if left > right:
                break

            # 从右到左
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            # 往上走
            bottom -= 1
            if top > bottom:
                break

            # 从下到上
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            # 往右走
            left += 1
            if left > right:
                break
