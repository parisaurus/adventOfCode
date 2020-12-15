file = open("input.txt", "r")


map = file.read().split("\n")
x, count = 0, 0
for aux in map:
    #print(len(aux))
    if aux[x] == "#":
        count += 1
    x = (x + 3) % len(aux)
print(count)