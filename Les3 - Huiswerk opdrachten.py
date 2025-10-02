#Huiswerk les 3
#Hfst 5

# a = 3
# b = 10
#
# if a > b:
#     print(a)
# else:
#     print(b)
#
# getal_1 = int(input("voer een getal in: "))
# getal_2 = int(input("voer een getal in: "))
# #veelvoud van het andere getal?
# if getal_1 % getal_2 == 0:
#     print("ja", getal_1, "is veelvoud van", getal_2)
# elif getal_2 % getal_1 == 0:
#     print(f"ja {getal_2} is veelvoud van {getal_1}")
# else:
#     print(f"nee {getal_1} en {getal_2} zijn geen veelvoud")
#
# print(50%5)
#
#
# leeftijd = int(input("voer je leeftijd in: "))
# basisprijs = 12
#
# if leeftijd < 5:
#     korting = 100
#     print(basisprijs *(1-korting/100))
# elif 5 <= leeftijd < 12:
#     korting = 50
#     print(basisprijs *(1-korting/100))
# elif 13 <= leeftijd <54:
#     korting = 0
#     print(basisprijs *(1-korting/100))
# elif leeftijd > 55:
#     korting = 100
#     print(basisprijs *(1-korting/100))
# else:
#     print(basisprijs)
# #2e optie
# leeftijd = int(input("voer je leeftijd in: "))
# basisprijs = 12
#
# if leeftijd < 5:
#     prijs = 0
# elif 5 <= leeftijd < 12:
#     prijs = basisprijs / 2
# elif 13 <= leeftijd < 54:
#     prijs = 12
# else:
#     prijs = 0
#
# print(f"voor de leeftijd {leeftijd} is de prijs: {prijs}")
#
#
# num1 = int(input("vul een getal in: "))
# num2 = int(input("vul nog een getal in: "))
# num3 = int(input("vul een laatste getal in: "))
# if num1 > num2:
#     num1,num2 = num2,num1
# if num2 > num3:
#     num2,num3 = num3, num2
# if num1 > num3:
#     num1,num3 = num3,num1
# if num3 < num1:
#     num1,num3 = num3,num1
# if num3 < num2:
#     num2,num3 = num3,num2
# if num2 < num1:
#     num1,num2 = num2,num1
# print(num1,num2,num3)

# #Opgave 4
# totaal = 0
# aantal_te_printen_getallen = 0
# #dit is voor het gemiddelde uit te rekenen.
# #als voor 'getal' wordt ingevuld: '5+7+8' dan staat 'aantal_te_printen_getallen op '3'
#
# getal = int(input("vul een getal in: "))
# while getal!=0:
#     totaal += getal
#     aantal_te_printen_getallen +=1
#     getal = int(input("vul een getal in: "))
# if getal==0:
# ### if aantal_te_printen_getallen !=0: << DIE SNAP IK NIET
#     print(f"totaal: {totaal} en gemiddelde: {totaal / aantal_te_printen_getallen}")
# else:
#     print("er zijn geen getallen ingevoerd") << DEZE WERKT NIET

# #Opgave 5
# factor = int(input("vul een getal in: "))
# for teller in range (1,11):
#     print(f"{teller} X {factor} = {teller*factor}")
#
# #Hfst 6 6.1 incl. Python Buku
# friends = ["Chandler,Joey,Phoebe,Monica,Rachel,Ross"]
# for friend in friends:
#     print("Hello", friend)
#
# friends = ["Chandler","Joey","Phoebe"]
# for friend in friends:
#     print("Hello", friend)
#
list_of_int = [2,5,7,11,15]
print(sum(list_of_int))

total = 0
for numm in [2,5,7,11,15]:
    total=total+numm
print("total: ",total)


# #6.2
tafel_van_drie = [3,6,9,12,16,18,24,27,32]
# tafel_van_drie.insert(4,15)
# tafel_van_drie.remove(16)
tafel_van_drie[4]=15
tafel_van_drie.remove(32)
tafel_van_drie.append(30)
tafel_van_drie.insert(6,21)
print(tafel_van_drie)

#6.3
namen = ['alfred','bob','charlie','david','erik']
print(namen[:3])
print(len(namen)-1)
print(namen[4])
print(", ".join(namen))
for friend in namen:
    print(friend)
namen[0]="Alice"
print(namen)

namen[3:] = ['daphne','eva','frederique']
print(namen)

#6.4
lijst = [getal for getal in range (1,21) if getal not in (1,3,5,7,9,11,13,15,17,19)]
print(lijst)

lijst = [getal for getal in range (1,21) if getal %2 ==0]
print(lijst)

student1= ('rood',)
student2= ('geel')
print(type(student1))
print(type(student2))

kleuren1 = {'rood','blauw','geel'}
kleuren2 = {'wit','geel','rood','oranje'}
kleuren3 = kleuren2.difference(kleuren1)
print(kleuren3)

list_of_names = ("Alice", "Dennis", "Ruby")
print(f"de laatste letter van de laatste naam is: {list_of_names[-1][-1]}")
print("de eerste letter van de laatste naam is: ", list_of_names[-1][0])