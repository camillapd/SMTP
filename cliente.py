from socket import *

def main():

    serverName = "localhost"
    serverPort = 25
    conexao = True
    enviando_dados = False

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    mensagem_recebida = clientSocket.recv(1024)
    print(mensagem_recebida.decode('utf8'))

    while(conexao):
        
        while(enviando_dados):
            
            mensagem_enviada = input()
            mensagem_enviada = mensagem_enviada.encode()       
            clientSocket.send(mensagem_enviada)

            if(mensagem_enviada.decode('utf-8')=="."):
                enviando_dados = False
                mensagem_recebida = clientSocket.recv(1024)
                print(mensagem_recebida.decode('utf8'))
                break             
            
        mensagem_enviada = input("C: ")

        if(mensagem_enviada=="QUIT"):
            conexao = False

        mensagem_enviada = mensagem_enviada.encode()
        clientSocket.send(mensagem_enviada)

        mensagem_recebida = clientSocket.recv(1024)
        print(mensagem_recebida.decode('utf8'))

        mensagem_str = mensagem_recebida.decode('utf8').split(' ')

        if(mensagem_enviada.decode('utf8')=="DATA" and mensagem_str[1]=="354"):
            enviando_dados = True

    clientSocket.close()
    
if __name__ == '__main__':
    main()