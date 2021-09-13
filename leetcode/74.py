def searchMatrix(matrix: [[int]], target: int) -> bool:
    """
    二分查找
    :param matrix:
    :param target:
    :return:
    """
    int_start = 0
    int_end = len(matrix) * len(matrix[0]) - 1
    while int_start <= int_end:
        int_mid = (int_start + int_end) // 2
        mid = [int_mid // len(matrix[0]), int_mid % len(matrix[0])]
        if matrix[mid[0]][mid[1]] > target:
            int_end = int_mid - 1
        elif matrix[mid[0]][mid[1]] < target:
            int_start = int_mid + 1
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target))