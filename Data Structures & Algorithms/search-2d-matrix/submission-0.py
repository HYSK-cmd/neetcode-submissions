class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return first_binary_search(matrix, target, 0, len(matrix)-1)
        
def first_binary_search(matrix, target, l, r):
    if l > r:
        return False
    mid = (l+r) // 2
    if target in matrix[mid]:
        row = mid
        return second_binary_search(matrix, target, row, 0, len(matrix[row])-1)
    if matrix[mid][-1] < target:
        return first_binary_search(matrix, target, mid+1, r)
    else:
        return first_binary_search(matrix, target, l, mid-1)

def second_binary_search(matrix, target, row, l, r):
    if l > r:
        return False
    mid = (l+r) // 2
    if target == matrix[row][mid]:
        return True
    if matrix[row][mid] < target:
        return second_binary_search(matrix, target, row, mid+1, r)
    else:
        return second_binary_search(matrix, target, row, l, mid-1)