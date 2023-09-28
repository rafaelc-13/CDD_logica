#Faça um código que receba as 3 notas de um aluno e
#verifique se ele está aprovado ou reprovado.
#Considere que a média para aprovação é 7,0, e a da recuperação 4,0

nome = input("Qual seu nome: ")
n1 = float(input("Qual a primeira nota: "))
n2 = float(input("Qual a primeira nota: "))
media = (n2+n1)/2

if media < 7:
    if media >= 4:
        print(nome, "sua média é: ",media," por isso, está de recuperação.")
    else:
        print(nome, "sua média é: ",media," por isso, está reprovado")
else:
    print(nome, "sua média é: ",media," por isso, está aprovado")
