var = int(input('Write natural number N:'))
var_1 = 0
var_2 = var
while var_2 > 0:
    var_1 += 1
    var_2 //= 10
for i in range(1, var + 1):
    for degree in range(1, var_1 + 1):
        if i == i * i % 10 ** degree:
            print(i, '*', i, '=', i * i)
            break