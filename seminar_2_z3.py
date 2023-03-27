n = int(input("Введите число n: "))
i = 0
print(f"Степени двойки от 0 до {n} будут равны: ")
while 2 ** i <= n:
    print(2 ** i)
    i += 1
