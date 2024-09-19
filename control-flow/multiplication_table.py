x, y = (1, 11)
number = int(input("enter a number to see its multiplication table: "))
print(f"|Multiplication table for (number):")
for i in range (1, 11):
    print(f"{number} * {i} = {number * i}")
