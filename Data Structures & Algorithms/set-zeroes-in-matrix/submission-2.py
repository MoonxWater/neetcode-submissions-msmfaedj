'''
keep a weight array equal to column of the matrix
1. run a loop over each row and check if the element is zero
2. if the current element is zero, make the corresponding
    weight zero
3. after inner loop, make the entire row zero

4.run another loop and multiply each element with the 
    corresponding weight
Note: In place, return None
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        size = len(matrix[0])
        weights = [1] * size

        for i in range(len(matrix)):
            found = False

            for j in range(size):
                if matrix[i][j] == 0:
                    weights[j] = 0
                    found = True
            if found:
                # matrix[i] = [0] * len(matrix[i])
                # the above would only refresh ref and not mod in place
                for j in range(size):
                    matrix[i][j] = 0
                # the above would mod in place which is what
                # we want
        
        for i in range(len(matrix)):
            for j in range(size):
                matrix[i][j] *= weights[j]
        