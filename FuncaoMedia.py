#função para armazenar notas digitadas pelo usuário
def leitura():
    #armazenamento da nota digitada
    nota = float(input("Digite uma nota: "))
    return nota


#função para cálculo utilizando dois valores de variáveis como parâmetro
def calculo(n1,n2):
    #cálculo da média
    media = (n1 + n2) / 2
    #print das duas notas, média e resultado com condicional
    print("\nNota 1: ", n1)
    print("Nota 2: ", n2)
    print("\nMédia: ", media)
    print("Resultado: ", end="")

    #condicional para determinar se o aluno foi aprovado ou reprovado
    if media >= 7.0:
        print("O aluno está aprovado")
    else:
        print("O aluno foi reprovado")


#armazenamento dos valores em "nota1" e "nota2"; em seguida cálculo usando as variáveis recém criadas como parâmetro
nota1 = leitura()
nota2 = leitura()
calculo(nota1,nota2)
