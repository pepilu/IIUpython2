import json
import csv
from lib2to3.pgen2.token import RPAR
from os import sep


lista_studenata = {
    "studenti": []
}
with open("studenti.csv", mode="r", encoding="utf-8", newline="") as std_fajl:
    # postavljamo newline="" kako nam se ne bi stvarali nepotrebni novi redovi
    # ovo nije mnogo bitno kod citanja koliko kod pisanja u csv fajl, gde je svaki red novi podatak
    reader = csv.DictReader(std_fajl)
    for row in reader:
        lista_studenata["studenti"].append(row)

# ovde vidimo da se u listi nalaze recnici
for dict in lista_studenata['studenti']:
    print(dict, sep='\n')


with open("studenti.json", mode="w", encoding="utf-8") as std_json:
    # dump sluzi za ubacivanje objekta u JSON
    json.dump(lista_studenata, std_json, ensure_ascii=False, indent=2)
    # ensure_ascii=False nam služi da se utf-8 karakteri sačuvaju

f = open("studenti.json", encoding="utf-8")
studenti = json.load(f)
print(*studenti["studenti"], sep="\n")

novi_student = {
    "ime": "Petar",
    "prezime": "Petrović",
    "indeks": "2022/1111",
    "smer": "ISIT"
}
# dump pretvara objekat u JSON string
json_obj = json.dumps(novi_student, ensure_ascii=False)
with open("novi_student.json", mode="w", encoding="utf-8") as outfile:
    outfile.write(json_obj)
