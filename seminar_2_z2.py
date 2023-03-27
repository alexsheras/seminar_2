import itertools
S = int(input("Введите сумма двух чисел, которые задумал Петя? : "))
P = int(input("Введите произведение двух чисел, которые задумал Петя? : "))
for X, Y in itertools.product(range(S), range(P)):
    if S == X + Y and P == X * Y:
                print(X, Y)