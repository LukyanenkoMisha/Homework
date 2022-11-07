counter = int(input())

print(counter, end= "  ")

for i in range(1, counter+1):
    if i ** 2 <= counter:
        print(i ** 2, end= " ")
