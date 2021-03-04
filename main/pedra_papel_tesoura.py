import random
import time


def jotnex():
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    print('''Suas opções:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA''')
    es = int(input('DIGITE AQUI: '))
    x = random.choice(lista)
    if es == 1:  # JOGADOR ESCOLHEU PEDRA
        print('JO...')
        time.sleep(0.6)
        print('KEN...')
        time.sleep(0.6)
        print('PO...!!')
        time.sleep(0.6)
        if x == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
            print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(x))
        elif x == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
            print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(x))
        elif x == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
            print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PEDRA!!'.format(x))
    elif es == 2:  # JOGADOR ESCOLHEU PAPEL
        print('JO...')
        time.sleep(0.6)
        print('KEN...')
        time.sleep(0.6)
        print('PO...!!')
        time.sleep(0.6)
        if x == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
            print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(x))
        elif x == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
            print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(x))
        elif x == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
            print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador PAPEL!!'.format(x))
    elif es == 3:  # JOGADOR ESCOLHEU TESOURA
        print('JO...')
        time.sleep(0.6)
        print('KEN...')
        time.sleep(0.6)
        print('PO...!!')
        time.sleep(0.6)
        if x == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
            print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(x))
        elif x == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
            print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(x))
        elif x == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
            print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                  '\nO computador escolheu {} \ne o jogador TESOURA!!'.format(x))
    else:  # NENHUMA DAS OPÇÕES
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
        print('\033[31m                         OPÇÃO INVÁLIDA\033[m')
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
    keep = ' '
    while keep != 'sim' and keep != 's' and keep != 'n' and keep != 'não' and keep != 'nao':
        keep = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if keep == 'sim' or keep == 's':
            jotnex()
        else:
            break


if __name__ == '__main__':
    jotnex()
