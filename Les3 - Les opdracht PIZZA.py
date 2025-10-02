#1 Maak een pizza
Toppings = ["kaas","ananas","ham","ui","salami"]

#2 Laat je pizza zien
print(f"De eerste topping op mijn pizza is {Toppings[0]}")
print(f"De derde topping op mijn pizza is {Toppings[2]}")
print(f"De laatste topping op mijn pizza is {Toppings[-1]}")
print(f"Mijn pizza bevat de volgende toppings: {Toppings}")
print(f"Mijn pizza bevat de volgende toppings: {", ".join(Toppings)}")

#extra
# for pizza in Toppings:
    #print(pizza)

#3 Extra topping
extra_toppings = input("Welke extra topping wil je?\n")
Toppings.append(extra_toppings)
print(f"De laatste topping op mijn pizza is nu: {Toppings[-1]}")
print(f"Mijn pizza bevat nu de volgende toppings: {Toppings}")
print(f"Mijn pizza bevat nu de volgende toppings: {", ".join(Toppings)}")

#4 Verwijder een topping
minder_toppings = input("Welke pizza topping vind je niet lekker?\n")
if minder_toppings in Toppings:
    Toppings.remove(minder_toppings)
    print(f"{minder_toppings} is verwijderd. De pizza bevat nu de volgende toppings: {", ".join(Toppings)}. Geniet van je pizza!")
else:
    print(f"{minder_toppings} was geen topping optie. De pizza bevat de volgende toppings: {", ".join(Toppings)}. Geniet van je pizza!")