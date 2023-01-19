import numpy as np

def printMatrix(matrix: np.ndarray):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(int(matrix[i][j]), end =(" " if j != len(matrix[i]) - 1 else "\n"))

if __name__ == "__main__":
    matrix = np.zeros((3,3))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                matrix[i][j] = 1 if (i == j) else 0

    printMatrix(matrix)
    print()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i != j):
                matrix[i][j] = matrix[i][j] + 3

    printMatrix(matrix)
    print()

    matrix2 = np.delete(matrix, len(matrix[0]) - 1, 1)
    
    printMatrix(matrix2)