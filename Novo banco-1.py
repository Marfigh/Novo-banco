senha=0
tentativas=2    
sacar= 0
depositar = 0
saldo = 0
tentativas2=2
print('****************************************')
print('*        Banco Master Brasil           *')
print('****************************************')
print('Seja bem vindo ao MELHOR banco do Brasil')
nome=input('Qual seu nome?\n')
print('Seja Muito bem vindo {} ao nosso banco'. format(nome))
print('Vamos criar um login bem rápido pra você está bem?')
print('Vamos criar uma senha e um endereço de email bem rapído ok\n')
email=input('Digite seu email ou gmail\n')
senha=int(input('Agora crie uma senha de números inteiros\n'))
print('Tudo pronto {} agora só entrar\n'. format(nome))
print('########### Menu de login ###########\n')
email2=input('Digite o email cadrastrado\n')
while email2 != email:
    print('Erro. Email não cadastrado ou errado')
    email2=input('Digite um email válido\n')
if email2 == email:
    print('Tudo certo {} com o email agora vamos para senha\n'. format(nome))
senha2=int(input('Digite a senha cadastrada\n'))
while senha2 != senha:
    if tentativas >= 1:
        tentativas=tentativas - 1
        print('Senha invalida')
        senha2=int(input('Digite a senha cadrastrada\n'))
    if tentativas <=0:
        print('Conta bloqueada, tente novamente em breve')
if senha2 == senha:
    print('Agora está tudo certo para comerçarmos')
    print('Seja Bem - Vindo(a) {}\n'. format(nome))
while True:
    print('------------- Menu de Escolhas -------------\n')
    print('1 - Consultar Saldo')
    print('2 - Sacar')
    print('3 - Depositar')
    print('4 - Trocar de senha')
    print('5 - Extrato')
    print('6 - Voltar \n')
    escolha=int(input('Escolha uma opção\n'))
    while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6:
        print('Escolha uma opção válida')
        escolha=int(input('Digite novamente\n'))
    if escolha == 1:
        print('Seu saldo é de {} R$'. format(saldo))
    elif escolha == 2:
        sacar=float(input('Qaunto você quer sacar?\n'))
        while sacar > saldo:
            print('Saldo insuficiente')
            sacar=float(input('Digite um valor de saque válido\n'))
        if sacar <= saldo:
            saldo=saldo - sacar
            print('Tudo certo com sua transação')
    elif escolha == 3:
        depositar=float(input('Quanto você quer depositar?\n'))
        saldo=saldo + depositar
        print('Tudo certo com sua transação')
    elif escolha == 4:
        senha3=int(input('Digite sua atual senha\n'))
        while senha3 != senha:
            while tentativas2 >= 1:
                if senha3 != senha:
                    tentativas2=tentativas2 - 1
                    print('Senha invalida')
                    senha3=int(input('Digite a senha cadrastrada\n'))
            if tentativas2 <=0:
                print('Conta bloqueada')
        if senha3 == senha:
            senha=int(input('Digite sua nova senha\n'))
            print('Tudo certo com a tarnsição de senha')
    elif escolha == 5:
        print('========== EXTRATO ========== \n')
        print('*último depósito = R$ {}'. format(depositar))
        print('*Último saque = R$ {}\n'. format(sacar))
        print('Saldo atual = R$ {}'. format(saldo))
    if tentativas2 <= 0:
        print('Tente novamente mais tarde')
    if tentativas2 >=1:
        voltar=int(input('Se deseja voltar ao menu digite 1 se não digite 2\n'))
        while voltar != 1 and voltar != 2:
            print('Opção inválida')
            voltar=int(input('Digite novamente\n'))
        if voltar == 1:
            print('')
    else:
        break

    






