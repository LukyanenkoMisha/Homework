calendar = int(input('Enter the year: '))

if calendar not in range(1901,1_000_000):
    print('Try again')
elif calendar % 4 == 0 and calendar % 100 != 0 or calendar % 400 == 0:
    print(calendar, "Is leep year")
else:
    print(calendar, "Is not leep year")