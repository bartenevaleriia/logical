A = int(input('Введите первое число диапазона '))
B = int(input('Введите второе число диапазона '))

if A % 2 == 0:
    even_1 = A
    odd_1 = A + 1
else:
    even_1 = A + 1
    odd_1 = A

if B % 2 == 0:
    even_2 = B
    odd_2 = B - 1
else:
    even_2 = B - 1
    odd_2 = B

if even_1 <= even_2:
    all_even = (even_2 - even_1) // 2 + 1
    sum_even = (even_1 + even_2) * all_even // 2
else:
    sum_even = 0

if odd_1 <= odd_2:
    all_odd = (odd_2 - odd_1) // 2 + 1
    sum_odd = (odd_1 + odd_2)* all_odd // 2
else:
    sum_odd = 0

difference = sum_even - sum_odd

if difference == 0:
    print('Суммы четных и нечетных чисел в этом диапазоне равны')
elif difference < 0:
    print('Сумма нечетных чисел в этом диапазоне больше')
else:
    print('Сумма четных чисел в этом диапазоне больше')