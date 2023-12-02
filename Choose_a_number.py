import random

print('Добро пожаловать в числовую угадайку')
max_x = int(input('Введите максимальное число: '))

r = random.randint(1, max_x)
print(r)

def is_valid(x):
  return x.isdigit() and 1 <= int(x) <= max_x


count = 0
while True:
  x = input(f'Введите число от 1 до {max_x}: ')
  if is_valid(x):
    x = int(x)
    if x < r:
      print('Ваше число меньше загаданного, попробуйте еще разок')
      count += 1
    elif x > r:
      print('Ваше число больше загаданного, попробуйте еще разок')
      count += 1
    else:
      count += 1
      print(f'Вы угадали, поздравляем! Количество попыток: {count}')
      answer = input('Ещё разок сыграем? да/нет: ')
      if answer == 'да':
        max_x = int(input('Введите максимальное число: '))
        r = random.randint(1, max_x)
        print(r)
        count = 0
        continue
      elif answer == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
  else:
    print(f'А может быть все-таки введем целое число от 1 до {max_x}?')
