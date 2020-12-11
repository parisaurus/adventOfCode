file = open("input.txt", "r")

#part1

def letterCount(letter, word, minMax):
    list_of_letters = list(word)
    count = 0
    for x in list_of_letters:
        if letter[:-1] == x:
            count += 1
    return count >= int(minMax[0]) and count <= int(minMax[1])

lista =file.read().split("\n")
contador = 0
for x in lista[:-1]:
    aux = x.split(" ")
    minMax = aux[0].split("-")
    if letterCount(aux[1], aux[2], minMax):
        contador += 1
print(contador)

#part2

def letterCount2(letter, word, minMax):
    list_of_letters = list(word)
    print(letter[:-1])
    
    return ((letter[:-1] == list_of_letters[minMax[0]]) ^ (letter[:-1] == list_of_letters[minMax[1]]))

lista =file.read().split("\n")
contador = 0
for x in lista[:-1]:
    aux = x.split(" ")
    minMax = aux[0].split("-")
    if letterCount2(aux[1], aux[2], minMax):
        contador += 1
print(contador)