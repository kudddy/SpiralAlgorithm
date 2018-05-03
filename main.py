# SpiralAlgorithm
import unittest
'''
 Для матрицы 2n-1 на 2n-1 выводит значения \
 на экран в ряд, начиная из центра по спирали:  \
 влево - вниз - вправо - вверх и т.д.
'''
def getSpiral(arr):

    arrayWidth = len(arr[0])
    arrayHeight = arrayWidth

    minX = 0
    minY = 0
    maxX = arrayWidth - 1
    maxY = arrayHeight - 1

    answer = []

    while (minX != maxX):
        for i in range(minX,maxX+1):
           answer.append(arr[minY][i])
        for i in range(minY+1,maxY+1):
            answer.append(arr[i][maxX])
        for i in range(maxX - 1,minX-1,-1):
            answer.append(arr[maxY][i])
        for i in range(maxY - 1,minY,-1):
            answer.append(arr[i][minX])
        minX = minX+1
        maxX = maxX-1
        minY = minY+1
        maxY = maxY-1
    answer.append(arr[minX][minY])
    return answer


"UnitTest"
class TestMethods(unittest.TestCase):

    def test_matrix(self):
        spiral = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [5, 4, 7, 8, 9, 6, 3, 2, 1]
        answer = getSpiral(spiral)
        answer.reverse()
        self.assertEqual(answer, expected)

        spiral = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]

        expected = [13, 12, 17, 18, 19, 14, 9, 8, 7, 6, 11, 16, 21, 22, 23, 24, 25, 20, 15, 10, 5, 4, 3, 2, 1]

        answer = getSpiral(spiral)
        answer.reverse()
        self.assertEqual(answer, expected)

        spiral = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42],
            [43, 44, 45, 46, 47, 48, 49]
        ]

        expected = [25, 24, 31, 32, 33, 26, 19, 18, 17, 16, 23, 30, 37, 38, 39, 40, 41, 34, 27, 20, 13, 12, 11, 10,
                    9, 8, 15, 22, 29, 36, 43, 44, 45, 46, 47, 48, 49, 42, 35, 28, 21, 14, 7, 6, 5, 4, 3, 2, 1]

        answer = getSpiral(spiral)
        answer.reverse()

        self.assertEqual(answer, expected)



if __name__ =='__main__':
    unittest.main()
