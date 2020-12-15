file = open("input.txt", "r")
text = file.read().split("\n\n")

def validate(text, i):
    necessaryFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for items in necessaryFields: 
        if items not in text[i]:
            #print("Item ", i, " missing ", items)
            return True

#number of items in the text
aux = 0
for items in text:
    aux = aux + 1

#bucle
for i, item in enumerate(text):
    if validate(text, i):
        aux = aux - 1



print("Number correct passports = ", aux )