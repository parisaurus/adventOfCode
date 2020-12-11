file = open("input.txt", "r")

#print(file.read())
lista = [int(x) for x in file.read().split("\n")]

#part1
for x in range(len(lista)):
    for j in range(x,len(lista)):
        if(lista[x] + lista[j]) == 2020:
            print(lista[x] * lista[j])

#part2
for x in range(len(lista)):
    for j in range(x,len(lista)):
        for k in range(j,len(lista)):
            if(lista[x] + lista[j] + lista[k]) == 2020:
                print(lista[x] * lista[j] * lista[k])