n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

sum = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div_int =  n1 // n2
rest = n1 % n2
exp = n1 ** n2

print ("A soma entre: ", n1," e ",n2," é: ",sum,
        "\nA subtração entre: ",n1," e ",n2," é ",sub,
        "\nA multiplicação entre: ",n1," e ",n2," é ",mult,
        "\nA divisão entre: ",n1," e ",n2," é ",div,
       "\nA parte inteira da divisão entre: ",n1," e ",n2," é ",div_int, #só considera a parte inteira da  divisão
       "\nO resto entre: ",n1," por ",n2," é ",rest,
       "\n",n1," elevado a ",n2," é ",exp)

