number_of_inputs = int(input("enter n: "))

square_array = [int(x) for x in input("enter squares array: ").split()]

day_month = [int(x) for x in input("enter day and month: ").split()]
day, month = day_month[0], day_month[1]

if month > number_of_inputs:
    output = 0
else:
    output = 0
    for i in range(number_of_inputs - month + 1):
        temp = 0
        for ii in range(i, i + month):
            temp += square_array[ii]
        if temp == day:
            output += 1

print(output)