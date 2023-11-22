def buscaBin (vetor, tam, valor):
    inicio = 0
    fim = tam-1
    while inicio <= fim:
        meio = int((inicio + fim)/2)
        if vetor[meio] == valor:
            return meio
        elif vetor[meio] > valor:
            fim = vetor[meio] - 1
        else:
            inicio = vetor[meio] + 1
    return -1

def leitura(tam):
    vetor = [0]*tam
    for i in range (tam):
        vetor[i] = int(input(f'Informe o {i +1}º valor positivo, ordenado do menor para o maior: '))
        while vetor[i] < 0:
            vetor[i] = int(input(f'Informe o {i +1}º valor positivo, ordenado do menor para o maior: '))
        while vetor[i] < vetor[i -1]:
            vetor[i] = int(input(f'Informe o {i +1}º valor positivo, ordenado do menor para o maior: '))
    return vetor

qntNum = int(input('Insira a quantidade de número que deseja alocar em um vetor: '))
vet = leitura(qntNum)
val = int(input('Qual o valor que gostaria de descobrir a posição vetorial? '))
busca = buscaBin(vet, qntNum, val)

if busca == -1:
    print(f'O valor {val} não está presende no vetor.')
else:
    print(f'O valor {val} foi encontrado na posição {busca} do vetor {vet}.')

