var1 = 10
var2 = 15
var3 = var1

print(var1, var2)

var1, var2 = var2, var1

print(var1, var2)

var1 = var2
print(var1, var2, var3)
var2 = var3
print(var1, var2)

var1, var2 = var2, var1

var1 = var1 * var2
var2 = var1 / var2
var1 = var1 / var2

print(var1, var2)


