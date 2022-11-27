titulo = ('\033[1;34mTABUADA \033[1;33mPYTHON')
print(titulo.center(40))
print()
nome = input('\033[mDigite Seu Nome: ').title()
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
        titulo =('TABUADA COMPLETA')
        print(titulo.center(152))
        for i in range(1, 11):
            print(f'\n1 + {i:2} = {1 + i:2}', f'\t2 + {i:2} = {2 + i}', f'\t3 + {i:} = {3 + i}', f'\t4 + {i:2} = {4 + i}', 
            f'\t5 + {i:2} = {5 + i}',f'\t6 + {i:2} = {6 + i}', f'\t7 + {i:2} = {i + 7}', f'\t8 + {i:2} = {8 + i}',
            f'\t9 + {i:2} = {9 + i}', f'\t10 + {i:2} = {10 + i}')
