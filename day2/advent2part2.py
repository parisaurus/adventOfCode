file = open("input.txt", "r")

def letterCount2(letter, word, minMax):
    list_of_letters = list(word)
    return (list_of_letters[int(minMax[0])-1] == letter[:-1]) ^ (list_of_letters[int(minMax[1])-1] == letter[:-1])


lista =file.read().split("\n")
contador = 0
for x in lista:
    aux = x.split(" ")
    minMax = aux[0].split("-")
    if letterCount2(aux[1], aux[2], minMax):
        contador += 1
print(contador)