



'''
X = [l.strip() for l in open('in\\1.txt')]
for elf in ('\n'.join(X)).split('\n\n'):
    for line in elf.split('\n'):
        asd =1 # do logic here
'''


# add the numbers together until line is empty then update max
f = open('in\\1.txt', "r")

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