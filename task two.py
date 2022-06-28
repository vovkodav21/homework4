import collections
num_set = set()
x = 1
while x != 0:
    x = int(input('введіть число: '))
    num_set.add(x)
aver_num_set = sum(num_set) / len(num_set)
aver_num_setround = round(aver_num_set,2)
max_val = 0
idx = None
for i, row in enumerate(num_set):
    if max(num_set) > max_val:
        max_val = max(num_set)
        idx = i
even_count, odd_count = 0, 0
for num in num_set:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
largest = max(num_set)
res = collections.Counter(num_set)

print(res[largest]) #визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
print("парних чисел в списку: ",even_count)
print("непарних чисел в списку: ", odd_count)
print(f"max value: {max_val}, at row: {idx}") #Визначити значення та порядковий номер найбільшого елемента послідовності. Якщо найбільших елементів є кілька,виведіть порядковий номер першого з них. Нумерація елементів починається з 1 (однини)
print(aver_num_set) #середнє арифметичне (крім завершального числа 0)
print(max(num_set)) #Визначити значення другого за величиною елемента в цій послідовності
print(len(num_set)) #кількість введених чисел (завершальний 0 не рахується)
print(sum(num_set)) #їхню суму



