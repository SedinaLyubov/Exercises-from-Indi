#  A. Красивая матрица 
#  Перед Вами матрица размера 5 × 5, состоящая из 24-x нулей и единственной единицы. Строки матрицы пронумеруем числами от 1 до 5 сверху вниз, столбцы матрицы пронумеруем числами от 1 до 5 слева направо. За один ход разрешается применить к матрице одно из двух следующих преобразований:

# Поменять местами две соседние строки матрицы, то есть строки с номерами i и i + 1 для некоторого целого i (1 ≤ i < 5).
# Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j + 1 для некоторого целого j (1 ≤ j < 5).
# Вы считаете, что матрица будет выглядеть красиво, если единственная единица этой матрицы будет находиться в ее центре (в клетке, которая находится на пересечении третьей строки и третьего столбца). Посчитайте, какое минимальное количество ходов потребуется, чтобы сделать матрицу красивой.

# Входные данные

# Входные данные состоят из пяти строк, в каждой из которых записаны пять целых чисел: j-ое число в i-ой строке входных данных обозначает элемент матрицы, стоящий на пересечении i-ой строки и j-ого столбца. Гарантируется, что матрица состоит из 24-x нулей и единственной единицы.

# Выходные данные

# Выведите единственное целое число — минимальное количество действий, которое требуется, чтобы сделать матрицу красивой.

a, b, c, d, e = (list(map(int, input().split())) for i in 'abcde')
sp = [a, b, c, d, e]
c = 0
for i in range(5):
  for j in range(5):
    if sp[i][j] == 1:
      while i != 2 or j != 2:
        if i < 2:
          i += 1
          c += 1
        if i > 2:
          i -= 1
          c += 1
        if j < 2:
          j += 1
          c += 1
        if j > 2:
          j -= 1
          c += 1    
        
print(c)

# Состязания
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем считается тот спортсмен, у которого сумма результатов по всем броскам максимальна.
# Если перенумеровать спортсменов числами от 0 до n-1, а попытки каждого из них – от 0 до m-1, то на вход программа получает массив A[n][m], состоящий из неотрицательных целых чисел. Программа должна определить максимальную сумму чисел в одной строке и вывести на экран эту сумму и номер строки, для которой достигается эта сумма.

# Входные данные

# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.

# Выходные данные

# Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается. Если таких строк несколько, то выводится номер наименьшей из них. Не забудьте, что нумерация строк (спортсменов) начинается с 0.

m, n = map(int, input().split())
a = []

for i in range(m):
    a.append(list(map(int, input().split())))

s = 0

for i in range(m):
  c = 0
  for j in range(n):
    c += a[i][j]
  if c > s:
    s = c
print(s)
for i in range(m):
  c = 0
  for j in range(n):
    c += a[i][j]
  if c == s:
    print(i)
    break







# # Миша и негатив
# # Миша уже научился хорошо фотографировать и недавно увлекся программированием. 
# Первая программа, которую он написал, позволяет формировать негатив бинарного черно-белого изображения.

# # Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо черным, либо белым. 
# Негатив такого изображения получается путем замены каждого черного пикселя на белый, а каждого белого пикселя – на черный.

# # Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться некорректный негатив. 
# Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению, Миша начал тестировать свою программу.

# # В качестве входных данных он использовал исходные изображения. 
# Сформированные программой негативы он начал тщательно анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.

# # Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение и полученный Мишиной программой негатив, 
#   и на основе этого определяет количество пикселей, в которых допущена ошибка.

# # Программа сперва считывает числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного изображения (в пикселях). 
# Последующие n строк содержат описание исходного изображения. Каждая строка состоит из m символов «B» и «W». 
# Символ «B» соответствует черному пикселю, а символ «W» – белому. 
# Далее следует пустая строка, а после нее – описание выведенного Мишиной программой изображения в том же формате, что и исходное изображение.
# Необходимо вывести на экран число пикселей негатива, которые неправильно сформированы Мишиной программой.
  
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(str, ' '.join(input().split()))))
input()
s = []
for i in range(m):
    s.append(list(map(str, ' '.join(input().split()))))
c = 0
for i in range(m):
  for j in range(n):
    if a[i][j] == s[i][j]:
      c += 1
print(c)


# Заполнение змейкой
# Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

# Входные данные
# Программа получает на вход два числа n и m.

# Выходные данные
# Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.

# Sample Input 1:

# 4 10
# Sample Output 1:

# 0  1  2  3  4  5  6  7  8  9
# 19 18 17 16 15 14 13 12 11 10
# 20 21 22 23 24 25 26 27 28 29
# 39 38 37 36 35 34 33 32 31 30

m, n = map(int, input().split())
a = []

c = 0
for i in range(m):
  b = []
  for j in range(n):
    b.append(c)
    c += 1
  a.append(b)
for i in range(1, m, 2):
  a[i].reverse()
for i in a:
  print(*i)


# A. Тортминатор
# Дан прямоугольный торт, который имеет вид таблицы размером r × c. 
# Каждая ячейка таблицы содержит либо гадкую клубничку, либо является пустой. 

# Тортминатор намерен съесть этот торт! 
# Каждый раз, когда он ест, он выбирает строку или столбец, не содержащие гадкой клубнички, а содержащие по крайней мере одну несъеденную ячейку торта. 
# Затем Тортминатор поедает все выбранные им ячейки торта. Тортминатор может есть сколько угодно раз. 
# Пожалуйста, выведите максимальное количество ячеек, которые может съесть Тортминатор.

# Входные данные
# Первая строка содержит два целых числа r и c (2 ≤ r, c ≤ 10), обозначающих количество строк и количество столбцов в торте. 
# Следующие r строк содержат по c символов — j-ый символ i-ой строки обозначает содержимое ячейки в строке i и столбце j, и имеет одно из следующих значений:

# символ '.' обозначает ячейку торта без гадкой клубнички;
# символ 'S' обозначает ячейку торта с гадкой клубничкой.
# Выходные данные
# Выведите максимальное количество ячеек торта, которые может съесть тортминатор.

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(str, ' '.join(input().split()))))
   
c = 0
for j in range(n): 
  v = []
  for i in range(m):
    v.append(a[i][j])
  for k in v:
    if 'S' in v:
      break
    else:
      c += 1
  for i in range(m):
    if 'S' not in v:
      a[i][j] = '0'
for i in range(m):
  x = []
  for j in range(n):
    x.append(a[i][j])
  for j in range(n):
    if 'S' not in x and a[i][j] == '.':
      c += 1
print(c)
