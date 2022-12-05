X = [l.strip() for l in open('in\\5.txt')]

stacks = [['b', 'v', 's', 'n', 't', 'c', 'h', 'q'], ['w', 'd', 'b', 'g'], ['f', 'w', 'r', 't', 's', 'q', 'b'], ['l', 'g', 'w', 's', 'z', 'j', 'd', 'n'], [
    'm', 'p', 'd', 'v', 'f'], ['f', 'w', 'j'], ['l', 'n', 'q', 'b', 'j', 'v'], ['g', 't', 'r', 'c', 'j', 'q', 's', 'n'], ['j', 's', 'q', 'c', 'w', 'd', 'm']]


# remove the starting position from input
for i in range(10):
    X.pop(0)



for move in X:
    move = move.split(" ")
    n = int(move[1])
    source = int(move[3])-1
    dest = int(move[5])-1

    list_to_move = stacks[source][-n:]
    stacks[source] = stacks[source][:-n]
    # list_to_move.reverse()
    stacks[dest] = stacks[dest] + list_to_move
    

for stack in stacks:
    print(stack[-1], end="")

