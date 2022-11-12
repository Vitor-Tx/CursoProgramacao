lista = input().split(" ")

for i in range(0, len(lista)):
    lista[i] = float(lista[i])


media = (lista[0]*2 + lista[1]*3 + lista[2]*4 + lista[3])/10
print(f"Media: {media}")
if(media>=7.0):
    print("Aluno aprovado.")
elif(media<5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame}")
    if((media+exame)/2 >= 5.0):
        print("Aluno aprovado.")
        print(f"Media final: {(media+exame)/2}")
    else:
        print("Aluno reprovado.")
        