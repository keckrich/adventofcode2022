

f = open("day2\input.txt", "r")


# add the numbers together until line is empty then update max

'''
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
'''


def choosemove(p1, p2):
    if p2 == "Y":
        return chr(ord(p1)+23)
    if p1 == "A":
        if p2 == "X":
            return "Z"
        else:
            return "Y"
    if p1 == "B":
        if p2 == "X":
            return "X"
        else:
            return "Z"
    if p1 == "C":
        if p2 == "X":
            return "Y"
        else:
            return "X"


sum = 0 
for line in f:
    p1 = line[0]
    p2 = line[2]
    p2 = choosemove(p1, p2)
    if ord(p1) == ord(p2)-23:
        sum += ord(p1) + 3 - 64
    elif p1 == "A" and p2 == "Y":
        sum += 2+6
    elif p1 == "A" and p2 == "Z":
        sum += 3
    elif p1 == "B" and p2 == "X":
        sum += 1
    elif p1 == "B" and p2 == "Z":
        sum += 3+ 6
    elif p1 == "C" and p2 == "X":
        sum += 1 + 6
    elif p1 == "C" and p2 == "Y":
        sum += 2

print(sum)