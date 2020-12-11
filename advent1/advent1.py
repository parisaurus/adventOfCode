file = open("input.txt", "r")

#print(file.read())
lista = [int(x) for x in file.read().split("\n")]

for x in range(len(lista)):
    for j in range(x,len(lista)):
        if(lista[x] + lista[j]) == 2020:
            print(x * j)