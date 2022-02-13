# https://github.com/belain3d/Fun-Projects #

# Összegzés függvény: összegzi egy adott lista/számsor számait | Sum of list elements.

def osszegzes(lista):
    osszeg = 0
    for i in lista:
        osszeg += i
    return osszeg

# Megszámlálás függvény: Megszámolja, hogy egy adott listában/sorban hány elem van | Counts the number of elements of the list.

def megszamlalas(lista):
    osszeg = 0
    for i in lista:
        osszeg += 1
    return osszeg

# Eldöntés függvény: Megmutatja, hogy a 2. argumentumként beütött érték benne van-e a listában/sorban | Shows if second argument
# is in the list or not.

def eldontes(lista, keresett):
    n = len(lista)
    i = 0

    while i < n and lista[i] != keresett:
        i += 1

    if i < n:
        return True
    else:
        return False

# Kiválasztás függvény: Megnézi, hogy a 2. argumentumként beütött érték hanyadik az adott listában/sorban | Shows the second
# argument's place in the list.

def kivalasztas(lista, szam):
    try:
        i = 0
        n = len(lista)
        while lista[i] != szam:
            i += 1
        return i+1
    except IndexError:
        pass

# Maximum kiválasztás függvény: kimutatja a legnagyobb értéket egy adott számsorban | Shows the largest number in the sequence.

def maxKiv(lista):
    maxElem = lista[0]
    for elem in lista:
        if elem > maxElem:
            maxElem = elem
    return maxElem

# Minimum kiválasztás függvény: kimutatja a legkisebb értéket egy adott számsorban | Shows the smallest number in the sequence.

def minKiv(lista):
    minElem = lista[0]
    for elem in lista:
        if elem < minElem:
            minElem = elem 
    return minElem