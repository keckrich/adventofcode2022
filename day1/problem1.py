

f = open("day1\input.txt", "r")


# add the numbers together until line is empty then update max

max = 0
total = 0

for line in f:
    if line == "\n":
        if total > max:
            max = total
        total = 0
        continue
    total += int(line)

print(max)