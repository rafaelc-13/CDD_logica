#Receba 2 números do usuário e mostre eles em ordem crescente

n1 = int(input("Valor: "))
n2 = int(input("Valor: "))

if n1 != n2 :
    if n1 > n2 :
        print(n1," é maior que ",n2)
    else :
        print(n2," é maior que ",n1)
else :
    print(n1," é igual a ",n2)
