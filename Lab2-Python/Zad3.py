import time


def lowercase(tekst):
    tekst = tekst.lower()
    return tekst


def sjp(tekst):
    f = open('SJP.txt', 'r', encoding="utf8")
    b = False
    for line in f:
        if line == tekst+'\n':
            print("This word exists in SJP.")
            b = True
            break
    if b == 0:
        print("This word does not exist in SJP.")
    f.close()

# wprowadzanie tekstu


print("Enter any text: ")
txt = input()
start = time.time()

# sprawdzanie czy to jeden wyraz
# przyjmuje ze tekst ma miec konstrukcje zdania czyli np "Slowo(spacja)slowo(spacja)slowo(kropka/pytajnik itd)"
# a slowo to bedzie dowolny ciag znakow w zdaniu spelniajacym powyzsza konstrukcje
# jezeli jednak poda sie np 'mama.'/'mama,'/'mama?'/'mama!'
# to bedzie to zdanie z jednym slowem, zakonczone kropka/przecinkiem/wykrzyknik/pytajnik
# a kropka/przecinek... zostanie usunieta/y do dalszego sprawdzania
# jezeli jednak poda sie np 'mama.mama','mama,mama' itd (bez '.' itd na koncu) to zostanie to uznane za blad uzytkownika
# (zamierzał podac pare wyrazow oddzielonych kropka/przecinkiem itd) i zostanie to zaliczone jako wiele wyrazow
check = txt.split(' ')
if len(check) == 1:
    if txt == '':
        print("There is no word!")
        a = False
    elif '.' in txt:
        if txt[len(txt)-1] == '.':
            print("The text consists of one word, but it ends with '.', so the '.' will be removed.")
            txt = txt.split('.')[0]
            a = True
        else:
            print("The text does not consist of one word (it contains '.' so it's considered as more than one word).")
            a = False
    elif ',' in txt:
        if txt[len(txt)-1] == ',':
            print("The text consists of one word, but it ends with ',', so ',' will be removed.")
            txt = txt.split(',')[0]
            a = True
        else:
            print("The text does not consist of one word (it contains ',' so it's considered as more than one word).")
            a = False
    elif '!' in txt:
        if txt[len(txt)-1] == '!':
            print("The text consists of one word, but it ends with '!', so '!' will be removed.")
            txt = txt.split('!')[0]
            a = True
        else:
            print("The text does not consist of one word (it contains '!' so it's considered as more than one word).")
            a = False
    elif '?' in txt:
        if txt[len(txt)-1] == '?':
            print("The text consists of one word, but it ends with '?', so '?' will be removed.")
            txt = txt.split('?')[0]
            a = True
        else:
            print("The text does not consist of one word (it contains '?' so it's considered as more than one word).")
            a = False
    else:
        print("The text consists of one word.")
        a = True

elif len(check) == 2 and check[1] == '' and check[0] != '':
    print("The text consists of one word (you entered additional ' ' at the end of it).")
    txt = txt.split(' ')[0]
    a = True
elif len(check) == 2 and check[0] == '' and check[1] == '':
    print("You entered only ' ' which is not considered a word.")
    a = False
else:
    print("The text you entered does not consist of one word.")
    a = False

if a == 1:
    txt = lowercase(txt)
    sjp(txt)
print("Runtime: ", (time.time()-start))
