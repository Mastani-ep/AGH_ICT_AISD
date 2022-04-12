import os
import shutil
# tworzymy liste plikow w folderze, zakladam ze katalog zadanie1 znajduje sie w biezacej sciezce dostepu
files=list(os.listdir(os.getcwd()+"/zadanie1"))
print(files)
for i in files:
    first = i[0].upper()
    # tworzenie sciezki aktualnej pliku
    source = os.getcwd()+"/zadanie1/"+i
    # tworzenie nowej sciezki do pliku
    destination = os.getcwd()+"/zadanie1/"+first+"/"+i
    # przeniesienie pliku a jezeli odpowiedni katalog nie istnieje to go tworzymy
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        destination_1 = os.getcwd() + "/zadanie1/" + first
        os.mkdir(destination_1)
        shutil.move(source, destination)