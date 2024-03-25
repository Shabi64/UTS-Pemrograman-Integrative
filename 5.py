with open("input.txt", "r") as file:
    numbers = [float(line.strip()) for line in file]

total = sum(numbers)

formatted_total = "{:,.3f}".format(total)

print(formatted_total)
