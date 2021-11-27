from random import SystemRandom
from string import ascii_letters, digits
from os.path import join
from datetime import datetime
import hashlib


class Error(Exception):
    pass


class SizeError(Error):  # Criação de Erro para o tamanho da senha
    def __init__(self, message):
        self.message = message


def salva_senha(senha):  # Método de gravação de hash da senha em diretório escolhido pelo usuário
    criptografia_resposta = input('Deseja criptografar a senha em hash? [S/N] ').strip().upper()[0]
    diretorio = input('Digite o diretório desejado para o arquivo: ').strip()
    arquivo = open(join(diretorio, 'senhas.txt'), 'a')
    while criptografia_resposta not in 'SN':
        criptografia_resposta = input('Deseja criptografar a senha em hash? [S/N] ').strip().upper()[0]
    if criptografia_resposta == 'S':
        arquivo.write(f'{hashlib.sha1(senha.encode()).hexdigest()}\n')  # Criptografando a senha em hash com algoritmo sha1
    else:
        arquivo.write(f'{senha}\n')  # Salvando senha sem criptografia


def main():
    chars = ascii_letters + digits + 'çÇ!@#$%&*()-_++§"´`[]{}ªº~^,.<>;:/?°\\|'  # Registrando os caracteres desejados para a senha
    rnd = SystemRandom()

    print('-' * 60)
    print('Gerador de Senha Forte Aleatória by Neto')
    print('-' * 60)

    while True:
        try:  # Validando se a entrada é um número
            tamanho = int(input('Digite a quantidade de dígitos de sua senha (Mínimo de 8 caracteres): '))
            if tamanho < 8:  # Validando se o tamanho é maior que 8 caracteres
                raise SizeError('Tamanho menor que 8 caracteres')
        except ValueError as erro:
            print(f'Por favor, digite um número. Erro: {erro}')
        except SizeError as erro:
            print(erro)
        else:
            inicio = datetime.now()
            print('Senha gerada: ', end='')
            senha = ''.join(rnd.choice(chars) for i in range(tamanho))  # Geração da senha aleatória com os caracteres registrados
            print(senha)
            print(f'Senha gerada em: {datetime.now() - inicio}')
            resposta_gravacao = input('Deseja gravar essa senha em um arquivo? [S/N] ').strip().upper()[0]
            while resposta_gravacao not in 'SN':
                resposta_gravacao = input('Deseja gravar essa senha em um arquivo? [S/N] ').strip().upper()[0]
            if resposta_gravacao == 'S':  # Gravação da senha em arquivo
                salva_senha(senha)
            resposta = input('Quer gerar mais uma senha? [S/N] ').strip().upper()[0]
            while resposta not in 'SN':
                resposta = input('Quer gerar mais uma senha? [S/N] ').strip().upper()[0]
            if resposta == 'N':
                print('Encerrando...')
                break


if __name__ == '__main__':
    main()
