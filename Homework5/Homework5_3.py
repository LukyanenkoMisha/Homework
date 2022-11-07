average = 0
summ = 0
paired = 0
non_paired = 0
count = 0
var_max = 0
var_min = 0
while True:
    var = int(input())
    if var == 0:
        break
    else:
        count += 1
        summ += var
        average = summ / count
        if count == 1:
            var_min = var
            var_max = var
        elif var > var_max:
            var_max = var
        elif var < var_min:
            var_min = var
        if var % 2 == 0:
            paired += 1
        else:
            non_paired += 1
if count > 0:
    print('1. Sum of Nubmers =', summ)
    print('2. Average =', average)
    print('3. Max Number =', var_max, 'Min Number =', var_min)
    print('4. Amount of paired =', paired, 'Amount of not paired =', non_paired)