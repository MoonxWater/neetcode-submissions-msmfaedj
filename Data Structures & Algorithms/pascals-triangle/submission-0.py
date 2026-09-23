class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        past = [[1], [1, 1]]

        for row in range(2, numRows):
            past.append([1])

            for cell in range(1, row):
                res = past[-2][cell] + past[-2][cell - 1]
                past[-1].append(res)
            past[-1].append(1)

        return past[:numRows]