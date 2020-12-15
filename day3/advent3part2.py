file = open("example.txt", "r")

map = file.read().split("\n")
x, count, totalTrees = 0, 0, 1
lista = [1,3,5,7]
for iterations in lista:
    for aux in map:
        if aux[x] == "#":
            count += 1  
        x = (x + iterations) % len(aux)
    print(count)
    totalTrees *= count

    count = 0
    x = 0   

x, aux, count = 0, 0, 0
for aux in map:
    #print(len(aux))
    if aux[x] == "#":
        count += 1  
    x = (x + 1) % len(aux)
    continue

print(count)
totalTrees *= count

print(totalTrees)