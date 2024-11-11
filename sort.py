from random import randint as ri

start_list = []
for i in range(0,100):
    start_list.append(ri(0, 1_000_000))
start_list
len(start_list)
sorted_list = start_list

stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(sorted_list) - 1):
        if sorted_list[i] < sorted_list[i + 1]:
            swap = sorted_list[i]
            sorted_list[i] = sorted_list[i + 1]
            sorted_list[i + 1] = swap
            stop_flag =True 
print(sorted_list)

unsorted_list = start_list
sorted_list = []

while len(unsorted_list) > 0:
    max = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i] > max:
            max = unsorted_list[i]
    sorted_list.append(max)
    unsorted_list.remove(max)

print(sorted_list)