userCpf =''
userNome=''
userSenha=''
userSaldo = 0

while True:
    print('--- Bem-vindo à Agência XPTO --- ')
    print('\n')

    print("1 - Criar conta")
    print ("2 - Fazer login")
    print ("3 - Sair")
    print("\n")

    escolha = int(input("> Escolha: "))
    print('\n')

    if escolha == 1:
        if userNome =='' and userCpf =='' and userSenha =='':
            userNome = str(input('Digite seu nome: '))
            userCpf = str(input('Digite seu CPF: '))
            userSenha = str(input('Crie uma senha: '))
            print('Conta criada com sucesso!')
            print('\n')
        else:
            print("Voce ja tem uma conta")
            print("\n")

    elif escolha == 2:
        
        if userNome =='' and userCpf =='' and userSenha =='':
            print("Voce não possui uma conta, porfavor crie uma conta")
            print('\n')
        else:
            print('------------- FAÇA SEU LOGIN-----------------')
            cpf = str(input("CPF : "))
            senha = str(input("Senha : "))
            print("\n")
            if cpf == userCpf and senha == userSenha:
                print("Login bem-sucedido!")
                print("\n")





                while True:
                    print("-------------- MENU --------------------")
                    print('1 - Ver saldo')
                    print('2 - Depositar')
                    print('3 - Sacar')
                    print('4 - Transferir')
                    print('5 - Ver extrato')
                    print('6 - Sair')

                    escolhaMenu = int(input("> Escolha : "))
                    print("\n")

                    if escolhaMenu == 1:
                        print('Seu saldo: R$ ', userSaldo)

                    elif escolhaMenu == 2:
                        valorDeposito = float(input('Digite valor para depósito: '))
                        print("\n")
                        if valorDeposito > 0 :
                            userSaldo = userSaldo + valorDeposito
                        else:
                            print("esse valor e invalido tente novamente")
                            print('\n')

                    elif escolhaMenu == 3:
                        valorSacar = float(input('Digite valor para o saque :'))
                        if valorSacar > 0: 
                            if userSaldo > valorSacar:
                                userSaldo = userSaldo - valorSacar
                            else:
                                print("Você não possui essa quantia para sacar ")
                                print("\n")
                        else:
                            print("esse valor e invalido")
                            print("\n")
                    elif escolhaMenu == 4:
                        print("transferir")
                    elif escolhaMenu == 5:
                        print("ver extrato")
                    elif escolhaMenu == 6:
                        print(" Você saiu do Menu ")
                        break
                    else:
                        print(" essa opção não existe tente novamanete")
                        print("\n")






    
                
            else:
                print("senha ou cpf incorretos")
                print("\n")
            
        
    elif escolha == 3: 
        print("Você saiu. Tenha um Bom Dia")
        break
    else:
        print(" Essa opção não existe tente novamente")
        print("\n")


