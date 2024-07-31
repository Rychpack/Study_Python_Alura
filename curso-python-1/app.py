import os
restaurantes = []

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar Restaurante:\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    voltar_menu()
    

def listar_restaurante():
    os.system('cls')
    print('Listando restaurantes: \n')
    for restaurante in restaurantes:
        if(restaurante == False):
            print('Lista Vazia')
            voltar_menu()
    else:
        print(f'.{restaurante}')
        voltar_menu()
    
   

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

# Escolher opção
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)   
        match(opcao_escolhida):
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                print('Ativar restaurante')
            case _:
                finalizar_app()
    except Exception as e:
        print(f'Error: {e}')
        voltar_menu()  
    
        


# Menu Principal
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()