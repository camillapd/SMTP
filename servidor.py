from socket import *
from sys import argv, exit

def le_arquivos():
    
    lista = []

    try:
        nome_arquivo = argv[1]
    except IndexError:
        print("Faltou adicionar um arquivo")
        exit()

    try:
        file = open(nome_arquivo,"r")
    except OSError:
        print("Não foi possível abrir o arquivo", argv[1])
        exit()

    count = len(open(argv[1]).readlines())
    for i in range(count):
        lista.append(file.readline())

    file.close()

    for i in range(len(lista)):
        lista[i] = lista[i].replace("\n",'')

    for i in range(len(lista)):
        t = lista[i]
        file = open(t,"w")
        file.close()

    return nome_arquivo

def checa_usuario(nome_arquivo,nome_usuario):
    
    usuario_existe = False
    file = open(nome_arquivo,"r")

    for linha in file:
        linha = linha[:-1]
        if(nome_usuario == linha):
            usuario_existe = True

    file.close()
    
    return usuario_existe

def main():

    serverPort = 25
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("",serverPort))
    serverSocket.listen(1)

    nome_arquivo = le_arquivos()

    print("O servidor está pronto para receber conexões SMTP")
    
    while 1:

        flag = 0
        file = 0
        dest = "0"
        conexao = True
        recebendo_dados = False      
        connectionSocket, addr = serverSocket.accept()       

        print("S: 220 bol.com.br")
        mensagem_resposta = b"S: 220 bol.com.br"
        connectionSocket.send(mensagem_resposta)

        while(conexao):

            mensagem_recebida = connectionSocket.recv(1024)                    

            print("C: " + mensagem_recebida.decode('utf8'))
            mensagem_str = mensagem_recebida.decode('utf8').split(' ')
            mensagem_resposta = b"S500 Syntax error, command unrecognized"

            if(recebendo_dados):
                email = mensagem_recebida.decode('utf8')                   

                if(mensagem_recebida.decode('utf-8')=="."):                   
                    recebendo_dados = False
                    print("S: 250 Message accepted for delivery")
                    mensagem_resposta = "S: 250 Message accepted for delivery"
                    mensagem_resposta = mensagem_resposta.encode()
                    connectionSocket.send(mensagem_resposta)
                    file.close()
                    continue

                # continue, para não chegar até o final do loop
                
                file.write(email)
                file.write('\n')
                continue

            if(flag==0 and (mensagem_str[0]=="HELO" and len(mensagem_str)==2)):
                client_server = mensagem_str[1]
                print("S: 250 Hello " + client_server + ", pleased to meet you")
                mensagem_resposta = "S: 250 Hello " + client_server + ", pleased to meet you"
                mensagem_resposta = mensagem_resposta.encode()
                flag = 1
            elif(flag==1 and len(mensagem_str)==3 and (mensagem_str[0]=="MAIL" and mensagem_str[1]=="FROM:")):
                client = mensagem_str[2]
                print("S: 250 " + client + " ... Sender ok")
                mensagem_resposta = "S: 250 " + client + " ... Sender ok"
                mensagem_resposta = mensagem_resposta.encode()
                flag = 2
            elif(flag==2 and len(mensagem_str)==3 and (mensagem_str[0]=="RCPT" and mensagem_str[1]=="TO:")):
                dest = mensagem_str[2]
                usuario_existe = checa_usuario(nome_arquivo,dest)

                if(usuario_existe):
                    print("S: 250 " + dest + " ... Recipient ok")
                    mensagem_resposta = "S: 250 " + dest + " ... Recipient ok"
                    mensagem_resposta = mensagem_resposta.encode()
                    flag = 3
                else:
                    print("S: 550 Address unknown")
                    mensagem_resposta = b"S: 550 Address unknown"
                    flag = 2
            elif(flag==3 and (len(mensagem_str)==1 and mensagem_str[0]=="DATA")):
                print("S: 354 Enter mail, end with '.' on a line by itself")               
                mensagem_resposta = b"S: 354 Enter mail, end with '.' on a line by itself"
                recebendo_dados = True
                file = open(dest,"a")
                flag = 2
            elif(len(mensagem_str)==1 and mensagem_str[0]=="QUIT"):
                print("S: 221 bol.com.br closing connection")
                mensagem_resposta = b"S: 221 bol.com.br closing connection"
                conexao = False
            else:
                print("S: 500 Syntax error, command unrecognized")
                mensagem_resposta = b"S: 500 Syntax error, command unrecognized"
        
            connectionSocket.send(mensagem_resposta)

        print(" ")

        connectionSocket.close()

if __name__ == '__main__':
    main()