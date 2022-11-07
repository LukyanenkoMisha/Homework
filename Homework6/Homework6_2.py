string = input("Enter String : ")
char = input("Enter symbol : ")
var = 0
var_1 = 0

while string.find(char, var) > 0:
    print(string.find(char, var))
    var = string.find(char, var) + 1
    var_1 += 1

print("We found :", var_1)