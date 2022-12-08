X = open('in\\6.txt').read().strip()


for i in range(len(X)):
    letters = {X[i], X[i+1], X[i+2], X[i+3]}
    if len(letters) == 4:
        print(i+4)
        break

for i in range(len(X)):
    letters = {X[i+j] for j in range(14)}
    if len(letters) == 14:
        print(i+14)
        break