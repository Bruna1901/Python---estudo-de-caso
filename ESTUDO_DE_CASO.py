import os

from colorama import Fore, init
init(autoreset=True) 

banco_dados = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Precisone ENTER pra continuar...")




def mostrar_produtos():
    contador = 1                  
    for produtos in banco_dados:
            print(f'{contador} - {produtos}')
            contador += 1
  

def selecionar_menu (opcao): # arrumar o codigo pag controle 
    if (opcao =='1'):
        mostrar_produtos()
        adicionar_produto = input ('Nome do produto, valor, qtde: ')
        banco_dados.append(adicionar_produto)
        print (f"{Fore.BLUE} Informações adicionadas")        
  
    elif (opcao =='2'):
       mostrar_produtos()
       numero_pruduto = int(input("Digite o número do produto para editar: "))
       atualizaçao_pruduto = input("Atualize as informações do produto: ")
       banco_dados [numero_pruduto - 1 ] = atualizaçao_pruduto

    elif (opcao =='3'):
        mostrar_produtos() #exluir 
        numero_pruduto = int(input ("Digite o número do produto para excluão: "))
        del banco_dados [numero_pruduto - 1]
        print (f"{Fore.RED} Produto exluído") 
        

    elif (opcao =='4'): #estoque
        print(f"{Fore.YELLOW} Estoque: Produto - Preço - Qtde")
        mostrar_produtos()
        pausar()

    elif (opcao =='0'):
         print ("Saindo do sistema")
         exit(0)
    else:
         print(f"{Fore.RED} Opção incorreta, tente novamente")
          
def exibir_menu():
    limpar_tela()
    print(f"{Fore.BLUE} -------Menu-------")
    print(f"{Fore.BLUE} 1 - Adicionar produto")
    print(f"{Fore.BLUE} 2 - Atualizar produto")
    print(f"{Fore.BLUE} 3 - Excluir produto")
    print(f"{Fore.BLUE} 4 - Visualizar estoque")
    print(f"{Fore.BLUE} 0 - Sair do Sistema ")
    opcao = input('Escolha uma opção: ')
    selecionar_menu (opcao)
    exibir_menu()

exibir_menu()

