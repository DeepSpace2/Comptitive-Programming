print(' '.join(str(valid - input_array) for valid, input_array in zip([1, 1, 2, 2, 2, 8], map(int, input().split()))))