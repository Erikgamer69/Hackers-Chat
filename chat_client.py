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
"""
print(banner)
nickname = input("Choose your nickname: ")
ip = input("Choose IP you want to connect: ")
print("Default port is 5555")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
cliente.connect((ip, 5555))                            

def connection():
    while True:                                                
        try:
            message = cliente.recv(1024).decode('coded')
            if message == 'NICKNAME':
                cliente.send(nickname.encode('coded'))
            else:
                print(message)
        except:                                                
            print("Error occured")
            cliente.close()
            break
def note():
    while True:                                                
        message = '{}: {}'.format(nickname, input(''))
        cliente.send(message.encode('coded'))

connection_thread = threading.Thread(target=connection)              
connection_thread.start()
note_thread = threading.Thread(target=note)                   
note_thread.start()
