number_of_birds = int(input("enter number of birds sighted: "))
bird_arr = [int(x) for x in input("enter bird_arr: ").split()]

bird_dict = dict()
for i in sorted(set(bird_arr)):
    bird_dict[i] = bird_arr.count(i)

max_birb_id = sorted(bird_arr)[-1]
for i in reversed(bird_dict.keys()):
    if bird_dict[i] >= bird_dict[max_birb_id]:
        max_birb_count = bird_dict[i]
        max_birb_id = i

print(max_birb_id)