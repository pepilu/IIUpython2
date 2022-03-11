# Python ima funkcije za kreiranje, citanje, azuriranje i brisanje fajlova (CRUD operacije)

# Open file
# ako ne postoji kreirace ga
myFile = open('myfile.txt', 'w')

# Get some info
print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed)
print("Opening mode: ", myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
# ako ostavimo w mode onda ce da krene ispocetka da pise, nece da nastavi dalje
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP!')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
