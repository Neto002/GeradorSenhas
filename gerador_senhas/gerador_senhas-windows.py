import os.path
import hashlib
from random import SystemRandom
from string import ascii_letters, digits
from datetime import datetime


class Error(Exception):
    pass


class SizeError(Error):  # Criação de Erro para o tamanho da senha
    def __init__(self, message):
        self.message = message


def salva_senha(senha):  # Método de gravação de hash da senha em diretório escolhido pelo usuário
    criptografia_resposta = input('Deseja criptografar a senha em hash? [S/N] ').strip().upper()[0]
    nome_arquivo = input('Digite o nome do arquivo a ser gerado: ').strip()
    site = input('Essa senha é para o cadastro de qual site? (Pressione enter caso não queira compartilhar): ').strip()

    print("""Escolha um local para salvar o arquivo: 
            1- Área de Trabalho
            2- Downloads
            3- Documentos
            4- Digitar manualmente""")

    while True:
        escolha = int(input('Sua escolha: '))
        if 0 < escolha < 5:
            break

    diretorio = f'C:\\Users\\{os.getlogin()}\\Desktop' if escolha == 1 else f'C:\\Users\\{os.getlogin()}\\Downloads' \
        if escolha == 2 else f'C:\\Users\\{os.getlogin()}\\Documents'  # Selecionando o diretório do arquivo

    while True:
        try:  # Validando o diretório inserido pelo usuário
            if escolha == 4:
                diretorio = input('Digite o diretório desejado para o arquivo: ').strip()
            arquivo = open(os.path.join(diretorio, f'{nome_arquivo}.txt'), 'a')
        except FileNotFoundError:
            print('Diretório inválido')
        else:
            break

    while criptografia_resposta not in 'SN':
        criptografia_resposta = input('Deseja criptografar a senha em hash? [S/N] ').strip().upper()[0]

    if criptografia_resposta == 'S':  # Criptografando a senha em hash com algoritmo sha1
        arquivo.write(f'{hashlib.sha1(senha.encode("utf-8")).hexdigest()} - {site}\n' if site != '' else
                      f'{hashlib.sha1(senha.encode("utf-8")).hexdigest()}')
    else:
        arquivo.write(f'{senha} - {site}\n' if site != '' else f'{senha}')  # Salvando senha sem criptografia


def main():
    # Registrando os caracteres desejados para a senha
    chars = ascii_letters + digits + 'çÇ!@#$%&*()-_++§"´`[]{}ªº~^,.<>;:/?°\\|'
    rnd = SystemRandom()

    print('-' * 60)
    print('Gerador de Senha Forte Aleatória by Neto')
    print('-' * 60)

    while True:
        try:  # Validando se a entrada é um número
            tamanho = int(input('Digite a quantidade de dígitos de sua senha (Mínimo de 8 caracteres): '))
            if tamanho < 8:  # Validando se o tamanho é maior que 8 caracteres
                raise SizeError('Tamanho menor que 8 caracteres.')
        except ValueError:
            print(f'Por favor, digite um número.')
        except SizeError as erro:
            print(erro)
        else:
            inicio = datetime.now()
            print('Senha gerada: ', end='')
            senha = ''.join(
                rnd.choice(chars) for _ in range(tamanho))  # Geração da senha aleatória com os caracteres registrados
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
