while True:

    string = input("Enter 2 words :\n")
    string_1 = string.split(" ")

    if len(string_1) != 2 or not string_1[1].isalpha() or not string_1[0].isalpha():
        print("Data not correct enter 2 words")
    else:
        break

print(string_1[0][::-1].capitalize(), string_1[1][::-1].capitalize())

