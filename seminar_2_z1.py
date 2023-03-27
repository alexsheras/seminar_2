import random

n = random.randrange(1, 100, 1)
coin0 = random.randint(0, n)
coin1 = n - coin0
print(f"Количество монет: {n}, из них решки: {coin0}, орлы: {coin1}")

min_count = 0
if coin1 == 0 or coin0 == 0:
    print('Все монеты уже повернуты вверх одной стороной')
elif coin1 <= coin0:
    min_count = n - coin0
else:
    min_count = n - coin1
print(f"Минимальное количество монет, которые нужно перевернуть: {min_count}")