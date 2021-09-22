'''1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield'''


def odd_nums(n):
    for i in range(1, n + 2, 2):
        yield i


odd_to_15 = odd_nums(15)
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))


'''2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
 не используя ключевое слово yield.'''
# n = int(input('Type the number: '))
# odd_nums = (i for i in range(n+2) if i % 2 != 0)
# print(*odd_nums)

'''3. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>).
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке classes меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: 
(<tutor>, None)'''

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Егор']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
name_class = sorted((tutors, classes), key=len)
x = name_class[1]
if x == classes:
    while len(tutors) != len(classes):
        tutors.append(None)
else:
    while len(classes) != len(tutors):
        classes.append(None)
t_c = ((tutors[i], classes[i]) for i in range(len(x)))

# print(*t_c)
# print(type(t_c))
'''4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего'''

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
# print(result)

'''5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке'''

src_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_2 = [i for i in src_2 if src_2.count(i) == 1]
# print(result_2)
