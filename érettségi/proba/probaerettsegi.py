# print("1.feladat")
# egy=int(input("Kérem az első számot: "))
# ketto=int(input("Kérem a második számot:"))
#
# print("A %i és %i közül  %i a nagyobb." %(egy,ketto, egy if egy>ketto else ketto))
# print("2.feladat")
#
# def kodolas(_szoveg,_betu,_szam):
#     kod=""
#     szamlalo=1
#     if _betu not in _szoveg:
#         print("Ilyen betű nincs a szövegben")
#         return None
#
#     for sbetu in _szoveg:
#
#         if sbetu==_betu and szamlalo<=_szam:
#             kod+=str(ord(sbetu))
#             szamlalo += 1
#         else:
#             kod+=sbetu
#
#     return kod
#
# szoveg=input("Kérem írjon be egy mondatot: ")
# betu=input("A mondat melyik betűjét kódoljam? ")
# szam=int(input("Hány db ilyen betűt kódoljak? "))
#
# print("A kódolt szöveg a következő. ",kodolas(szoveg,betu,szam))
#3. feladat
kocsik=[]
with open('autok.csv', 'r', encoding='utf-8') as forras:
    forras.readline()
    for sor in forras:
        sor_lista=sor.strip().split(";")
        egy_kocsi={"indulas":sor_lista[0],"cel":sor_lista[1],"rendszam":sor_lista[2],"telefon":sor_lista[3],"hely":sor_lista[4]}
        kocsik.append(egy_kocsi)
#b.)Összesen hány férőhelyet hirdettek meg Munkács-Záhony útvonalra?
ossz_ferohely=0
for kocsi in kocsik:
    if kocsi["indulas"]=="Munkács" and kocsi["cel"]=="Záhony":
        ossz_ferohely+=int(kocsi["hely"])
print("3.b feladat: Összesen  Munkács-Záhony útvonalra %i férőhely áll rendelkezésre"%(ossz_ferohely))

# c.) Átlagosan hány férőhely van az autókban? Határozd meg 1 tizedesjegy pontossággal!
for kocsi in kocsik:
    ossz_ferohely+=int(kocsi["hely"])
print("3.c feladat: Átlagosan %f férőhely áll rendelkezésre"%(round(ossz_ferohely/len(kocsik),1)))
#Panni kirándulni szeretne menni Budapestről.
# Hova tud eljutni? Listázd ki a lehetséges úticélokat és a telefonszámokat
# egy UTF-8 kódolású “budapestrol.dat” nevű fájlba.
with open('budapestrol.dat', 'w', encoding='utf-8') as cel:
    for kocsi in kocsik:
        if kocsi["indulas"] == "Budapest":
            kiir=kocsi["indulas"]+";"+kocsi["cel"]+";"+kocsi["rendszam"]+";"+kocsi["telefon"]+";"+kocsi["hely"]
            print(kiir, file=cel)




