var = input()
var_1 = 0
for i in var:
    if var_1 == 2:
        break
    var_1 = 0
    for j in var:
        if j == i:
            var_1 += 1
if var_1 == 2:
    print("Yes")
else:
    print("No")