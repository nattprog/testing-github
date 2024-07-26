s_and_t = [int(x) for x in input("s and t: ").split()]
start, end = s_and_t[0], s_and_t[1]

a_and_b = [int(x) for x in input("a_and_b: ").split()]
locA, locO = a_and_b[0], a_and_b[1]

num_ao = [int(x) for x in input("numbers of ao: ").split()]
sizeA, sizeB = num_ao[0], num_ao[1]


distance_a = [int(x) for x in input("distance_a: ").split()]
apples = []
for x in range(sizeA):
    try:
        apples.append(distance_a[x])
    except:
        apples.append(0)

distance_o = [int(x) for x in input("distance_o: ").split()]
oranges = []
for x in range(sizeA):
    try:
        oranges.append(distance_o[x])
    except:
        oranges.append(0)

counterA = 0
for i in apples:
    if start <= (locA + i) <= end:
        counterA += 1

counterO = 0
for i in oranges:
    if start <= (locO + i) <= end:
        counterO += 1

print(f"{counterA}\n{counterO}")