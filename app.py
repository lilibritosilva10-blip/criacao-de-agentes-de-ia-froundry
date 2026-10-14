


        


# BANCO QUE FAZ DEPOSITO
# SAQUE
# VER O EXTRATO 

print('BANCO')
auto-py-to-exe
senha = '1234'
senha_input =  input('Senha: ')

acessar  =  input('Deseja acessar o banco? s/n')
saldo = 1000.00
extrato =  [1000.0]

while acessar ==    's':



    if senha_input == senha:

        print('Acesso autorizado...')
        menu =  ['','Saque','Deposito','Extrato']
        print(f'''
            
            1 - {menu[1]}
            2 - {menu[2]}
            3 - {menu[3]}       
            
            ''')
        escolha  = int(input('Escolha a operação: '))
        if escolha == 1:
            
            saque =  float(input('Saque R$ >>> '))    
            resto = saldo - saque
            print('R$', resto)
            extrato.append(-saque)
            acessar =  input('Deseja continuar? ')
        
        elif escolha  == 2:
            
            deposito =  float(input('Saque R$ >>> '))    
            resto = saldo + deposito
            print('R$', resto)
            extrato.append(deposito)
            acessar =  input('Deseja continuar? ')
            
        elif escolha  == 3:
            print('extrato', extrato)      
            acessar =  input('Deseja continuar? ')      
                
        
    else:
        print('Acesso negado...')    