from functools import reduce
my_list = [num for num in range(100, 1001, 2)]
print(reduce(lambda num_1, num_2: num_1 * num_2, my_list))
