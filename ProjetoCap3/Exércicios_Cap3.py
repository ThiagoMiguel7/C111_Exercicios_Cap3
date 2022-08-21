#Exércicio 1

print('\033[1m' + 'Exercício 1' + '\033[0m')

listaTimes = ['Real Madrid','Barcelona', 'Marchester United','Juventus','PSG']

print('\nOs 3 primeiros colocados são: ' , listaTimes[:3])
print('Os Últimos 2 colocados são: ',listaTimes[3:])
print('Lista em ordem alfabética: ',sorted (listaTimes))
print('O Barcelona se encontra na posição ', listaTimes.index('Barcelona'), ' da tabela.')

#Exércicio 2

print('\n\033[1m' + 'Exercício 2' + '\033[0m')

loja_1 = {'Samsung Galaxy S22 Ultra','Apple iPhone 12','Apple iPhone 13 Pro Max','ASUS Zenfone 8','Xiaomi Poco X3 Pro'}
loja_2 = { 'Samsung Galaxy Z Fold 3','Motorola Moto G200', 'Xiaomi Redmi Note 11s', 'Samsung A53 5G', 'Apple iPhone 12 Pro'}

print('\nModelos disponiveis nas lojas: ',loja_1.union(loja_2))
print('Há', len(loja_1.union(loja_2)) , 'diferentes modelos disponíveis nas lojas.')
print('Loja A tem disponível: ', loja_1)
print('Loja B tem disponível: ', loja_2)

#Exércicio 3

print('\n\033[1m' + 'Exercício 3' + '\033[0m')

aluno ={}

print("Digite seu nome: ")
aluno[ 'Nome' ] = nome = input()

print("Digite sua média: ")
aluno [ 'Media' ] = float(input())

if aluno [ 'Media' ] >= 60:
    print('Situação Final: AP')
    aluno ['Situação Final'] = 'AP'
else:
    print('Situação Final: RP')
    aluno['Situação Final'] = 'RP'

print(aluno)


