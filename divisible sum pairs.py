n_and_k = [int(x) for x in input("enter n and k: ").split()]
n_iterations, k_divisor = n_and_k[0], n_and_k[1]

values = [int(x) for x in input("enter values of n integers: ").split()]

divisible_counter = 0

for it_j in range(len(values)):
    j = values[it_j]
    for it_i in range(it_j):
        i = values[it_i]
        if (i+j)/k_divisor == int((i+j)/k_divisor):
            divisible_counter += 1

print(divisible_counter)
