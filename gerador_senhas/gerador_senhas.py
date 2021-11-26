from random import SystemRandom
from string import ascii_letters, digits


class Error(Exception):
    pass


class SizeError(Error):
    def __init__(self, message):
        self.message = message


def main():
    chars = ascii_letters + digits + 'çÇ!@#$%&*()-_++§"´`[]{}ªº~^,.<>;:/?°\\|' #  Registrando os caracteres desejados para a senha
    rnd = SystemRandom()

    print('-'*60)
    print('Gerador de Senha Forte Aleatório by Neto')
    print('-'*60)

    while True:
        try:  #  Validando se a entrada é um número
            tamanho = int(input('Digite a quantidade de dígitos de sua senha (Mínimo de 8 caracteres): '))
            if tamanho < 8:  #  Validando se o tamanho é maior que 8 caracteres
                raise SizeError('Tamanho menor que 8 caracteres')
        except ValueError as erro:
            print(f'Por favor, digite um número. Erro: {erro}')
        except SizeError as erro:
            print(erro)
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
