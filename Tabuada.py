from time import sleep

def tabuada_soma():
    resp = input('Tabuada Completa? [SIM/NÃO] ').strip().upper()[0]
    print()
    sleep(1)
    if resp in 'Ss':
        titulo = ('TABUADA COMPLETA')
        print(titulo.center(152))
        for i in range(1, 11):
            print(f'\n1 + {i:2} = {1 + i:2}', f'\t2 + {i:2} = {2 + i}', f'\t3 + {i:} = {3 + i}', f'\t4 + {i:2} = {4 + i}', 
            f'\t5 + {i:2} = {5 + i}',f'\t6 + {i:2} = {6 + i}', f'\t7 + {i:2} = {i + 7}', f'\t8 + {i:2} = {8 + i}',
            f'\t9 + {i:2} = {9 + i}', f'\t10 + {i:2} = {10 + i}')
    else:
        print('Digite Dois Números especificos...')
        sleep(1)
        print()
        num = int(input('Digite o primeiro número: '))
        sleep(1)
        num_2 = int(input('Digite o segundo número: '))
        sleep(1)
        print()
        print(f'{num} + {num_2} = {num + num_2} ')

def tabuada_subtracao():
    resp = input('Tabuada Completa? [SIM/NÃO] ').strip().upper()[0]
    print()
    sleep(1)
    if resp in 'Ss':
        titulo = ('TABUADA COMPLETA')
        print(titulo.center(152))
        for i in range(1, 11):
            print(f'\n1 - {i:2} = {1 - i:2}', f'\t2 - {i:2} = {2 - i}', f'\t3 - {i:} = {3 - i}', f'\t4 - {i:2} = {4 - i}', 
            f'\t5 - {i:2} = {5 - i}',f'\t6 - {i:2} = {6 - i}', f'\t7 - {i:2} = {i - 7}', f'\t8 - {i:2} = {8 - i}',
            f'\t9 - {i:2} = {9 - i}', f'\t10 - {i:2} = {10 - i}')
    else:
        print('Digite Dois Números especificos...')
        sleep(1)
        print()
        num = int(input('Digite o primeiro número: '))
        sleep(1)
        num_2 = int(input('Digite o segundo número: '))
        sleep(1)
        print()
        print(f'{num} - {num_2} = {num - num_2} ')

def tabuada_multiplicacao():
    resp = input('Tabuada Completa? [SIM/NÃO] ').strip().upper()[0]
    print()
    sleep(1)
    if resp in 'Ss':
        titulo = ('TABUADA COMPLETA')
        print(titulo.center(152))
        for i in range(1, 11):
            print(f'\n1 x {i:2} = {1 * i:2}', f'\t2 x {i:2} = {2 * i}', f'\t3 x {i:} = {3 * i}', f'\t4 x {i:2} = {4 * i}', 
            f'\t5 x {i:2} = {5 * i}',f'\t6 x {i:2} = {6 * i}', f'\t7 x {i:2} = {i * 7}', f'\t8 X {i:2} = {8 * i}',
            f'\t9 x {i:2} = {9 * i}', f'\t10 x {i:2} = {10 * i}')
    else:
        print('Digite Dois Números especificos...')
        sleep(1)
        print()
        num = int(input('Digite o primeiro número: '))
        sleep(1)
        num_2 = int(input('Digite o segundo número: '))
        sleep(1)
        print()
        print(f'{num} x {num_2} = {num * num_2} ')

def tabuada_divisao():
    resp = input('Tabuada Completa? [SIM/NÃO] ').strip().upper()[0]
    print()
    sleep(1)
    if resp in 'Ss':
        titulo = ('TABUADA COMPLETA')
        print(titulo.center(152))
        for i in range(1, 11):
            print(f'\n1 : {i:2} = {1 / i:2}', f'\t2 : {i:2} = {2 / i}', f'\t3 : {i:} = {3 / i}', f'\t4 : {i:2} = {4 / i}', 
            f'\t5 : {i:2} = {5 / i}',f'\t6 : {i:2} = {6 / i}', f'\t7 : {i:2} = {i / 7}', f'\t8 : {i:2} = {8 / i}',
            f'\t9 : {i:2} = {9 / i}', f'\t10 : {i:2} = {10 / i}')
    else:
        print('Digite Dois Números especificos...')
        sleep(1)
        print()
        num = int(input('Digite o primeiro número: '))
        sleep(1)
        num_2 = int(input('Digite o segundo número: '))
        sleep(1)
        print()
        print(f'{num} : {num_2} = {num / num_2} ')



def main():
    
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
        tabuada_soma()
    elif opcao == 2:
        tabuada_subtracao()
    elif opcao == 3:
        tabuada_multiplicacao()


if __name__ == '__main__':
    main()