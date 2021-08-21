import socket
import threading                                                

banner = """                     
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝

            ██████╗██╗  ██╗ █████╗ ████████╗
           ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
           ██║     ███████║███████║   ██║
           ██║     ██╔══██║██╔══██║   ██║
           ╚██████╗██║  ██║██║  ██║   ██║
            ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
      [+Developed By Erik Gamer69#5895+]
                   [+LH+]
"""
host = input("Put here IP you want the chat to be hosted: ")                                                                                                           

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
servidor.bind((host, 5555))                                               
servidor.listen()

clientes = []
nicknames = []

def transmit(message):                                                 
    for client in clientes:
        client.send(message)

def resolv(client):                                         
    while True:
        try:                                                            
            message = client.recv(1024)
            transmit(message)
        except:                                                         
            index = clientes.index(client)
            clientes.remove(client)
            client.close()
            nickname = nicknames[index]
            transmit('{} lefted the chat'.format(nickname).encode('coded'))
            nicknames.remove(nickname)
            break

def conection():                                                          
    while True:
        client, address = servidor.accept()
        print("connected with this ip: {}".format(str(address)))       
        client.send('NICKNAME'.encode('coded'))
        nickname = client.recv(1024).decode('coded')
        nicknames.append(nickname)
        clientes.append(client)
        print("Nickname used is {}".format(nickname))
        transmit("{} Connected to server!".format(nickname).encode('coded'))
        client.send(' Connected to server!'.encode('coded'))
        thread = threading.Thread(target=resolv, args=(client,))
        thread.start()

print(banner)
conection()
