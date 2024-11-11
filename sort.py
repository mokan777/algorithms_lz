from random import randint as ri #вызываем функцию random

start_list = []  #создаем список в котором 100 элементов
for i in range(0,100): 
    start_list.append(ri(0, 1_000_000))
start_list
len(start_list) #проверяем кол-во элеменов

sorted_list = start_list
counter = 0
stop_flag = True
while stop_flag is True: #запускаем цикл while он остановится когда stop_flag = True
    stop_flag = False
    for i in range(0, len(sorted_list) - 1): #перебираем весь список начиная с 0 элемента и до 101, но от списка - 1 элемент и в итоге перебираем 100 элементов 
        for y in range(0, len(sorted_list) - 1): 
          counter += 1     
          if sorted_list[i] < sorted_list[i + 1]:
            swap = sorted_list[i]
            sorted_list[i] = sorted_list[i + 1]
            sorted_list[i + 1] = swap
            stop_flag =True 
print(sorted_list)
print("кол-во сортировок",counter)

unsorted_list = start_list
sorted_list = []
counter_2= 0
while len(unsorted_list) > 0:
    max = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
     for t in range(0, len(unsorted_list)):
        counter_2 +- 1
        if unsorted_list[i] > max:
            max = unsorted_list[i]
    sorted_list.append(max)
    unsorted_list.remove(max)

print(sorted_list)
print("кол-во сортировок",counter_2)
