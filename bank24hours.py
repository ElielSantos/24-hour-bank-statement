from datetime import datetime

current_dateTime = datetime.now()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
data = datetime.now()

print()
print('....BEM-VINDO AO PROGRAMA DO BANCO CIPRESTE....')
#input para dados cliente
A = input("NOME COMPLETO:")
B = int(input('AGENCIA:'))
C = int(input('CONTA:'))

print('')
print('......DEMOSTRATIVO DE OPERAÇÃO......')
print('01010 BANCO 24 HORAS') #IMPRIMIR LOCAL PELO ID
print('DATA DA IMPRESSÃO =', current_dateTime.year) #DATA DO EXTRATO AQUI
print('CIPRESTE BANK S A')
print("HORA DE BRASILIA =", current_time) #HORA DA IMPRESSAO AQUI 
print('....................................') 

print('SALDO N. 0000000000000') #IMPRIME A QUANTIDADE DE EXTRATO NO DIA NO APP
print('BANCO CIPRESTE SALDO DA CONTA CORRENTE')
print('AGENCIA =',B)
print('CONTA =',C)
print(A)


print('www.ciprestebank.com.br')