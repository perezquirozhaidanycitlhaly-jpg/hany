#Haidany citlhaly perez quiroz
edad = int(input("Ingresa tu edad: "))
tiene_ine = input("¿Tienes INE? (s/n): ")

if edad >= 18 and tiene_ine == "s":
    print("Puedes votar")
else:
    print("No puedes votar")
