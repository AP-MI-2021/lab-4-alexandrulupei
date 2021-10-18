def coutlist(l):
    return l

def citireLista():
    '''
    Citeste o lista de nr intregi
    :return: lista citita
    '''
    l = []
    givenstring = (input("scrieti elem listei separate prin virgula"))
    numbers_as_string = givenstring.split(",")
    for x in numbers_as_string:
        l.append(int(x))
    return l


def primeNumbers(l):
    '''
    Determina o o noua lista fara elementele prime din lista data
    :param l: o lista de numere
    :return: elementele neprime din lista
    '''
    rezultat = []
    for x in l:
        ok = True
        if x<2:
            ok =False
        else:
            for i in range(2, x // 2 +1):
                if x% i == 0:
                    ok = False
        if ok is False:
            rezultat.append(x)
    return rezultat


def ifAverage(l, k):
    '''
     Determina dacă media aritmetică a numerelor este mai mare decât un număr n dat.
    :param l:o lista de numere
    :return:True daca media este mai mare decat k si False in caz contrar
    '''
    sum = 0
    index = 0
    avg = None
    for x in l:
        sum += x
    avg = sum / len(l)
    if avg > k:
        return True
    else:
        return False


def divisor(l):
    '''
    Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai
    elementului.
    :param l:o lista de numere
    :return:Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai
    elementului.
    '''
    rezultat = []
    for x in l:
        index = 0
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                index += 1
        rezultat.append(x)
        rezultat.append(index)
    return rezultat


def tuplex(l):
    '''
    Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe
    prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia
    poziție apare numărul de apariții a numărului.
    :param l:o lista de numere
    :return: un tuplu format din numar, index si numarul de aparitii
    '''
    thistuple = ()
    rezfinal = []
    index = 0
    for x in l:
        y = list(thistuple)
        y.append(x)
        y.append(index)
        y.append(l.count(x))
        index += 1
        thistuple = tuple(y)
        rezfinal.append(thistuple)
        thistuple = ()
    return rezfinal


def test_tuplex():
    assert tuplex([]) == []
    assert tuplex([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert tuplex([25, 13, 26, 13, 4]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2), (4, 4, 1)]

def test_divisor():
    assert divisor([]) == []
    assert divisor([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert divisor([19, 5, 24, 12, 9 , 0, ]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1, 0 , 0]

def test_primeNumbers():
    assert primeNumbers([]) == []
    assert primeNumbers([8, 19, 17, 25]) == [8,25]
    assert primeNumbers([1, 2, 5, 10, 17,22 ,13]) == [1,10,22]


def test_ifAverage():
    assert ifAverage([10, -3, 25, -1, 3, 25, 18], 10) is True
    assert ifAverage([1], 1) is False
    assert ifAverage([10, -3, 25, -1, 3, 25, 18], 1000) is False

def main():
    test_tuplex()
    test_primeNumbers()
    test_ifAverage()
    test_divisor()
    print(""""1,  Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente.
    2,  Afișarea listei după eliminarea numerelor prime din listă
    3,  Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.
    4,  Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai
        elementului.
    5,  Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe
        prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia
        poziție apare numărul de apariții a numărului.
    a,  Afisare lista
    x,  Iesire""""")

    while True:
        option = input("Selectati o optiune")
        if option == "1":
            l = citireLista()
        elif option == "2":
            print(primeNumbers(l))
        elif option == "3":
            n = int(input("Dati un numar:"))
            if ifAverage(l,n) is True:
                print("DA")
            else:
                print("NU")
        elif option == "4":
            print(divisor(l))
        elif option == "5":
            print(tuplex(l))
        elif option == "a":
            print(coutlist(l))
        elif option == "x":
            break

main()