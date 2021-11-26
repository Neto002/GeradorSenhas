from random import SystemRandom
from string import ascii_letters, digits


def main():
    chars = ascii_letters + digits + 'çÇ!@#$%&*()-_++§"´`[]{}ªº~^,.<>;:/?°\\|' #  Registrando os caracteres desejados para a senha
    rnd = SystemRandom()

    while True:
        try:  #  Validando se a entrada é um número
            tamanho = int(input('Digite a quantidade de dígitos de sua senha: '))
        except ValueError as erro:
            print(f'Por favor, digite um número. Erro: {erro}')
        else:
            print('Senha gerada: ', end='')
            print(''.join(rnd.choice(chars) for i in range(tamanho))) #  Geração da senha aleatória com os caracteres registrados
            resposta = input('Quer gerar mais uma senha? [S/N]').strip().upper()[0]
            while resposta not in 'SN':
                resposta = input('Quer gerar mais uma senha? [S/N]').strip().upper()[0]
            if resposta == 'N':
                print('Encerrando...')
                break


if __name__ == '__main__':
    main()
