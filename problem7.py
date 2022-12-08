X = [l.strip() for l in open('in\\7.txt')]

fs = {'/':[{}, 0, None]}
current_dir = [fs, 0, None]

total_size = 0
dir_sizes = []

for x in X:
    line = x.split(" ")
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                # calculate the size of the current directory
                current_dir[1] = sum([current_dir[0][f][1] for f in current_dir[0]])
                dir_sizes.append(current_dir[1])
                if current_dir[1] <= 100000:
                    total_size += current_dir[1]
                current_dir = current_dir[2]
            else:
                current_dir = current_dir[0][line[2]]
        else:
            # $ ls
            continue
    else:
        if line[0] == "dir":
            current_dir[0].update({line[1]: [{}, 0, current_dir]})
        else:
            current_dir[0].update({line[1]: [{}, int(line[0]), current_dir]})

        # current_dir[1] += int(line[0])

while current_dir[2] != None:
    current_dir[1] = sum([current_dir[0][x][1] for x in current_dir[0]])
    dir_sizes.append(current_dir[1]) 
    if current_dir[1] <= 100000:
        total_size += current_dir[1]
    current_dir = current_dir[2]

current_dir[1] = sum([current_dir[0][x][1] for x in current_dir[0]])

space_needed = current_dir[1] - (70000000 - 30000000)

dir_sizes = [x for x in dir_sizes if x >= space_needed]

# pprint.pprint(fs)
print(total_size)
print(min(dir_sizes))