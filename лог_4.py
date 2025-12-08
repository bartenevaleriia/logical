number = 179

x = number - 1  # т.к. считаем с 0, должно быть на 1 меньше

letter1 = x // 81  # делим на 3(основание системы счисления) в степени 4(расставили в обратном порядке над числами от 0 до 4)
left1 = x % 81

letter2 = left1 // 27  # делим на 3 в степени 3
left2 = left1 % 27

letter3 = left2 // 9 # 3 в степени 2
left3 = left2 % 9

letter4 = left3 // 3
left4 = left3 % 3

letter5 = left4

X=0
Y=1
Z=2

letters = ['X', 'Y', 'Z']
result = letters[letter1] + letters[letter2] + letters[letter3] + letters[letter4] + letters[letter5]

print(f'У 179 машины порядковый номер: {result}')



