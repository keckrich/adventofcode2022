

f = open("day1\input.txt", "r")


# add the numbers together until line is empty then update max

total = 0
top_three = [0, 0, 0]

for line in f:
    if line == "\n":
        current_min = min(top_three)
        if total > current_min:
            top_three.remove(current_min)
            top_three.append(total)
        total = 0
        continue
    total += int(line)

print("max: ", max(top_three))
print("sum of top three: ", sum(top_three))