while True:
    number = input("Enter number from 3 to 9:")

    if number.isdigit():
        number = int(number)
        if not 9 >= number >= 3:
            print("False")
        else:
            break
    else:
        print("False")

Data_string = "123456789"
pyramid = number * 2 + 1
while True:

    print(Data_string[0].ljust(pyramid))
    for i in range(1, number):
        a = Data_string[0:i + 1] + Data_string[i - 1::-1]
        print(a.ljust(pyramid))


    else:
        break
