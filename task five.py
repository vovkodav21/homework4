astring = str(input("Введіть рядок: "))
for el in range(0,len(astring)):
    if el % 2 == 0:
        print(astring[el])
    else:
        continue
#можна print(*astring[::2])
print(*astring[1::2])
print(astring[2]) #a. Виведіть третій символ цього рядка.
print(astring[-2]) # b. виведіть передостанній символ цього рядка.
print(astring[0:5]) #с. виведіть перші п'ять символів цього рядка.
print(astring[:-2]) #d. виведіть весь рядок, крім двох останніх символів.
print(astring[::-1])

