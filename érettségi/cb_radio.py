adasok=[]
with open('cb.txt', 'r', encoding='utf-8') as forras:
    forras.readline()
    for sor in forras:
        sor_lista=sor.strip().split(";")
        egy_sofor={"ora":sor_lista[0],"perc":sor_lista[1],"adas":sor_lista[2],"nev":sor_lista[3]}
        adasok.append(egy_sofor)
#print(adasok)
def AtszamolPercre(_ora,_perc):
    return str(int(_ora)*60+int(_perc))

print("3.feladat: Bejegyzések száma: %i db" %(len(adasok)))
print("4.feladat: ",end="")
van=False
for adat in adasok:
    if adat["adas"]=="4":
        van=True

        break
print("volt négy adást indító söfőr" if van else "Nincs ilyen adat")
print("5.feladat: ",end="")
snev=input("Kérek egy nevet: ")
szam=0
for adat in adasok:
    if adat["nev"]==snev:
        szam+=1
print(" %s %ix használta a CB-rádiót"%(snev,szam) if szam!=0 else "Nincs ilyen adat")

with open('cb2.txt', 'w', encoding='utf-8') as cel:
    print("Kezdes;Nev;AdasDb", file=cel)
    for sor in adasok:
        kiir=AtszamolPercre(sor["ora"],sor["perc"])+";"+sor["nev"]+";"+sor["adas"]
        print(kiir,file=cel)
print("8.feladat: ",end="")
nevek=[]
indit=[]
for adat in adasok:
    if adat["nev"] not in nevek:
        nevek.append(adat["nev"])
        indit.append(0)

print("sofőrök száma: %i fő" %(len(nevek)))

for adat in adasok:
    i=nevek.index(adat["nev"])
    indit[i]+=int(adat["adas"])
max=indit[0]
max_hely=0
for x in range(len(indit)):
    if indit[x]>max:
        max=indit[x]
        max_hely=x
print("9.feladat: Legtöbb adást indító sofőr")
print("Név:", nevek[max_hely])
print("Adások száma: ", max, "alkalom")

