# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
import os


list_number = []
def listar_numeros():
    item = float(input('Digite um valor: '))
    list_number.append(item)
    
def somar_numeros():
    soma_list = 0
    for numero in list_number:
        soma_list += numero 
    print(f'Soma: {soma_list}\n')
     
    

def media_numeros():
    soma_list = 0
    for numero in list_number:
        soma_list += numero  
    media = soma_list/len(list_number)
    print(f'Média: {media}\n')

def zerar_numeros():
    del list_number[0:]
    print(list_number)
 
   
try:
    def main():
        os.system('clear' or 'cls')
        while True:
            seletor = input('Digite ( listar / somar / media / zerar ): ')
            os.system('clear' or 'cls')
            match(seletor):
                case 'listar':
                    listar_numeros()
                    main() 
                case 'somar':
                    somar_numeros()    
                case 'media':
                    media_numeros()  
                case 'zerar':    
                    zerar_numeros()
                case _:
                    os.system('clear' or 'cls')   
                
    main()  
        
except ZeroDivisionError:
    print('Lista vazia')
except Exception as e:
    print(f'Error: {e}')

