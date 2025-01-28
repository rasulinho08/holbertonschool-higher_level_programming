def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each integer in the row, formatted with str.format()
        print(" ".join("{:d}".format(num) for num in row))
