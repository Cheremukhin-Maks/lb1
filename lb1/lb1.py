import timeit




print ("Task 1")
my_list = [1, 2, 3, 4, 5, 6, 7]
print(f"my_list: {my_list} ")
print("звернення до елементів за додатним і за від’ємним індексом")
print(my_list[4])
print(my_list[-1])
print("slice 1")
print(my_list[0:6:2])
print("slice 2")
print(my_list[9:0:-1])
print("slice 3")
print(my_list[::3])
print("Вставка за індексом")
my_list[3] = 10
print(my_list)
print("Додавання в кінець")
my_list.append(17)
print(my_list)
print("Видалення за індексом")
my_list.pop(2)
print(my_list)

print(" ")
print("###############################################################")
print("Task 2")
students = [(1, "Middle_name1", [90, 95]), (2, "Middle_name2", [100, 97]), (3, "Middle_name3", [71, 77])]
def unbox (student):
    group, middle_name, marks = student
    print(f"Група: {group}, Прізвище: {middle_name}, Оцінки: {marks}")

unbox(students[0])

def middle_mark (mark) -> float:
    all_marks = 0
    marks_sum = 0
    
    for marks in students:
       marks_list = marks[2]
       marks_sum += sum(marks_list)
       all_marks += len(marks_list)
    result = marks_sum/all_marks
    return(result)

print(f"Середня оцінка всіх студентів: {middle_mark(students)}")

print("Спроба змінити прізвище прямо в кортежі")
first_student = students[0]
try:
    first_student[1] = "New_Middle_name"
except TypeError:
    print("Error")

print("Додавання нової оцінки в список, що лежить всередині кортежу:")
print(f"Оцінки до зміни {first_student[2]}")
first_student[2].append(75)
print(f"Оцінки після зміни {first_student[2]}")

print(" ")
print("###############################################################")
print("Task 3")
print("Введіть текст, для завершення введення двічі натисніть Enter:")

lines = []
while True:
    str = input()
    if str == "":
        break;
    lines.append(str)

raw_text = " ".join(lines)
lowered_text = raw_text.lower()
punctuation = ".,!?;:-'\"()[]{}"
cleaned_text = ""
for char in lowered_text:
    if char in punctuation:
        cleaned_text += " "
    else:
        cleaned_text += char

words_list = cleaned_text.split()

frequency_dict = {}

for words in words_list:
    current_count = frequency_dict.get(words, 0)
    frequency_dict[words] = current_count + 1
print(frequency_dict)

print(" ")

filtered_dict = {words: count for words, count in frequency_dict.items() if count >= 2}
print(f"dict comprehension: {filtered_dict}")

print("Сортування за ключем")
for key, values in sorted(frequency_dict.items()):
    print(f"Кількість: {values}, Ключ: '{key}'")

print(" ")

print("Сортування за спаданням частоти")
sorted_by_frequency = sorted(frequency_dict.items(),key=lambda x: x[1], reverse = True)
for key, value in sorted_by_frequency:
    print(f"Зустрічається {value} раз(и) -> Слово: '{key}'")


print(" ")
print("###############################################################")
print("Task 4")

my_collection1 = [5, 7, 10, 75, 15, 27, 7, 20, 17, 15, 77]
my_collection2 = [77, 99, 101, 57, 342, 10, 5, 77, 993, 57, 99, 7]

set1 = set(my_collection1)
set2 = set(my_collection2)

print("множина унікальних значень")
print(f"set1: {sorted(set1)}")
print(f"set2: {sorted(set2)}")

print(" ")

print("Перетин")
print(sorted(set1 & set2))

print("Об'єднання")
print(sorted(set1 | set2))

print("Симетрична різниця")
print( sorted(set1 ^ set2))

print("Відношення підмножини")
print(set2.issubset(set1))

print(" ")
print("###############################################################")
print("Task 5")

n1 = 100_000
n2 = 10_000
n3 = 1000

test_list = list(range(n1))
test_set = set(range(n1))
test_dict = {i: i for i in range(n1)}
target1 = -1


time1_list = timeit.timeit(lambda: target1 in test_list, number = 10_000)
time1_set = timeit.timeit(lambda: target1 in test_set, number = 10_000)
time1_dict = timeit.timeit(lambda: target1 in test_dict, number = 10_000)
print("При n = 100000")
print(f"Пошук у Списку:  {time1_list:.7f} с")
print(f"Пошук у Множині: {time1_set:.7f} с")
print(f"Пошук у Словнику: {time1_dict:.7f} с\n")
print(f"set швидше за list у {time1_list/ time1_set:.0f} разів")

print(" ")
test_list2 = list(range(n2))
test_set2 = set(range(n2))
test_dict2 = {i: i for i in range(n2)}


time1_list2 = timeit.timeit(lambda: target1 in test_list2, number = 7000)
time1_set2 = timeit.timeit(lambda: target1 in test_set2, number = 7000)
time1_dict2 = timeit.timeit(lambda: target1 in test_dict2, number = 7000)
print("При n = 10000")
print(f"Пошук у Списку:  {time1_list2:.7f} с")
print(f"Пошук у Множині: {time1_set2:.7f} с")
print(f"Пошук у Словнику: {time1_dict2:.7f} с\n")
print(f"set швидше за list у {time1_list2/ time1_set2:.0f} разів")

print(" ")
test_list3 = list(range(n3))
test_set3 = set(range(n3))
test_dict3 = {i: i for i in range(n3)}


time1_list3 = timeit.timeit(lambda: target1 in test_list3, number = 500)
time1_set3 = timeit.timeit(lambda: target1 in test_set3, number = 500)
time1_dict3 = timeit.timeit(lambda: target1 in test_dict3, number = 500)
print("При n = 1000")
print(f"Пошук у Списку:  {time1_list3:.7f} с")
print(f"Пошук у Множині: {time1_set3:.7f} с")
print(f"Пошук у Словнику: {time1_dict3:.7f} с\n")
print(f"set швидше за list у {time1_list3/ time1_set3:.0f} рази")

print("Побудова структури унікальних значень з нуля при n = 1000")
def make_list():
    made_list = []
    for i in range(n3):
        if i not in made_list:
            made_list.append(i)
        else: continue

def make_set():
    made_set = set()
    for i in range(n3):
        made_set.add(i)

time_make_list = timeit.timeit(make_list, number = 70)
time_make_set = timeit.timeit(make_set, number = 70)

print(f"Час побудови Списку:  {time_make_list:.7f} с")
print(f"Час побудови Множини: {time_make_set:.7f} с")
print(f"set швидше за list у {time_make_list/ time_make_set:.0f} разів")
