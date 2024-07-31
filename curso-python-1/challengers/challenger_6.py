# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
import os

list_number = []
def listar_numeros():
    item = int(input('Digite um valor: '))
    list_number.append(item)

def somar_numeros():
    soma = 0
    for numero in list_number:
        soma += numero 
    print(f'Soma: {soma}\n')
   
def zerar_numeros():
    del list_number[0:]
    print(list_number)
     
try:
    def main():
        os.system('clear' or 'cls')
        while True:
            seletor = input('Digite ( listar / somar / zerar ): ')
            os.system('clear' or 'cls')
            match(seletor):
                case 'listar':
                    listar_numeros()
                    main()
                case 'somar':
                    somar_numeros() 
                case 'zerar':    
                    zerar_numeros()
                case _:
                    os.system('clear' or 'cls')
    main()  
except Exception as e:
    print(f'Error {e}')
    main()
                
                
            
    

    
            
    
        
         
    
    
    