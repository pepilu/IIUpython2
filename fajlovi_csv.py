import csv

#koristimo with statement kako ne bi morali da brinemo o zatvaranju fajlova
with open("studenti.csv", mode="r", encoding="utf-8", newline="") as std_fajl:
    # postavljamo newline="" kako nam se ne bi stvarali nepotrebni novi redovi
    # ovo nije mnogo bitno kod citanja koliko kod pisanja u csv fajl, gde je svaki red novi podatak

    # reader vraca listu sa listama
    reader = csv.reader(std_fajl)
    print(reader)
    for row in reader:
        print(row)


lista_studenata = []
with open("studenti.csv", mode="r", encoding="utf-8", newline="") as std_fajl:
    # postavljamo newline="" kako nam se ne bi stvarali nepotrebni novi redovi
    # ovo nije mnogo bitno kod citanja koliko kod pisanja u csv fajl, gde je svaki red novi podatak

    # DictReader vraca listu sa recnicima
    reader = csv.DictReader(std_fajl)
    for row in reader:
        lista_studenata.append(
            f'{row["ime"]} {row["prezime"]} | {row["indeks"]} | {row["smer"]}')

# stampanje iteratora u celosti sa definisanim separatorom, umesto for petlje
# * kao SPREAD ili REST operator u JS-u
# ** se koristi da isto kao SPREAD ili REST operator, samo sto ce ona da prosledi listu property-ja iz recnika, a nece vrednosti da prosledi
print(*lista_studenata, sep="\n")

lista_za_dodavanje = []
unos = input("Unesite podatke za studente. Ako zelite da prekinete unesite N ")
while unos != "N":
    student = {
        "ime": "",
        "prezime": "",
        "indeks": "",
        "smer": ""
    }
    student["ime"] = input("Ime> ")
    student["prezime"] = input("Prezime> ")
    student["indeks"] = input("Indeks> ")
    student["smer"] = input("Smer> ")

    lista_za_dodavanje.append(student)
    unos = input("Novi student?Y/N ")

with open("studenti.csv", mode="a", newline="", encoding="utf-8") as std_input:
    fieldnames = ["ime", "prezime", "indeks", "smer"]
    writer = csv.DictWriter(std_input, fieldnames=fieldnames)
    writer.writerows(lista_za_dodavanje)
