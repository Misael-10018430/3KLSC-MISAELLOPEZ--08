
MaxTeamC = 10
A = [0]*MaxTeamC
frente = 0
final = 0
contador = 0



respuesta = input("Desea ingresar elementos a la cola?: ").lower()
while respuesta == "s" and contador < 10: 
    if (final + 1) %MaxTeamC == frente: 
        print("Desbordamiento de la cola.")
        exit(1)
    elemento = input("Ingrese un elemento para la cola:")
    final = (final + 1) %MaxTeamC
    A[final]= elemento 

    contador += 1
    print(f"elemento (contador)agregando a la col: {elemento}")

    if contador < 10: 
        respuesta = input("Desea agregar mas elementos a la cola?. ").lower()

if frente == final: 
     print(" la cola esta vacia: ")
     exit(1)

primerelemento = A[(frente + 1) %MaxTeamC]
print(f"el primer elemento de la cola es: {primerelemento}")

frente = (frente + 1) %MaxTeamC

i = (frente + 1) % MaxTeamC
while i != (final + 1) %MaxTeamC:
    print(A[i], end= "")
    i = ( i + 1)%MaxTeamC
print()