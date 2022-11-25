titulo = ('\033[1;34mTABUADA \033[1;33mPYTHON')
print(titulo.center(40))
print()
nome = input('\033[mDigite Seu Nome: ')
print(f'Olá {nome}, Bem - Vindo a Tabuada Interativa!!')
print("""[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO""")
opcao = int(input('Escolha a operação desejada: '))
print()
if opcao == 1:
    resp = input('Tabuada Completa? [SIM/NÃO] ').strip().upper()[0]
    print()
    if resp in 'Ss':
        for i in range(1, 11):
            print(f'1 + {i:2} = {1 + i}', f'\t2 + {i:2} = {2+i}', f'\t3 + {i:} = {3+1}', f'\t4 + {i:2} = {4+i}', f'\t5 + {i:2} = {5+i}')