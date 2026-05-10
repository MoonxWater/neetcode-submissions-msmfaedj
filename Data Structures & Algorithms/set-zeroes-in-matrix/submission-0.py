'''
keep a weight array equal to column of the matrix
1. run a loop over each row and multiply each element 
    with the corresponding weight
2. if the current element is zero, make the corresponding
    weight zero
    3. make the entire row zero
Note: In place, return None
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        weights = [1] * len(matrix[0])

        for i in range(len(matrix)):
            found = False

            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    weights[j] = 0
                    found = True
            if found:
                matrix[i] = [0] * len(matrix[i])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] *= weights[j]
        