# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# 112 42 83 119
# 56 125 56 49
# 15 78 101 43
# 62 98 114 108

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0

    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])
    return s

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        print(matrix)
        result = flippingMatrix(matrix)

        print(result)
