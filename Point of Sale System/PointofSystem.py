# Importeer nodige module vir command line argumente
import sys

# Inisialiseer die lys om items te stoor
items = []

# Funksie om 'n item by die lys te voeg
def voeg_item_by(name, price):
    items.append((name, float(price)))
    print(f"Item {name} met prys {price} bygevoeg.")

# Funksie om 'n item uit die lys te verwyder
def verwyder_item(name):
    global items
    items = [item for item in items if item[0] != name]
    print(f"Item {name} verwyder indien dit bestaan het.")

# Funksie om alle items en die totaal te vertoon
def vertoon_items():
    print("\nProdukte en hul pryse:")
    total = 0
    for item in items:
        print(f"{item[0]}   R{item[1]:.2f}")
        total += item[1]
    print("---------------")
    print(f"Totaal R{total:.2f}\n")

# Hooffunksie om die POS-stelsel te laat loop
def main():
    while True:
        print("\nPOS Kieslys:")
        print("1. Voeg item by")
        print("2. Verwyder item")
        print("3. Vertoon items")
        print("4. Verlaat")

        choice = input("Kies 'n opsie: ")

        if choice == '1':
            name = input("Voer die itemnaam in: ")
            price = input("Voer die item prys in: ")
            voeg_item_by(name, price)
        elif choice == '2':
            name = input("Voer die itemnaam in om te verwyder: ")
            verwyder_item(name)
        elif choice == '3':
            vertoon_items()
        elif choice == '4':
            print("Verlaat POS-stelsel.")
            break
        else:
            print("Ongeldige keuse. Probeer asseblief weer.")

# Laat die hooffunksie loop as hierdie skrip uitgevoer word
if __name__ == "__main__":
    main()
