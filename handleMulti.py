import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message='HTTP/1.0 200 OK \n\n'
nok_message ='HTTP/1.0 404 NotFound\n\n'
def process_start(s_sock):
s_sock.send(str.encode(welcome))
welcome=["Welcome to Server"]
while True:
data=s_sock.recv(2048)
print(data)
if not data:
break
s_sock.sendall(str.encode(ok_message))
s_sock.close()

if_name_=='_main_':
s=socket.socket(socke.AF_INET,socket.SOCK_STREAM)
s.bind(("",8888))
print("Listening....")
s.listen(3)
try:
while True:
try:
s_sock, s_addr=s.accept()
p=Process(target=process_start, args=(s_sock,))
p.start()
except socket.error:
print("Got a Socket Error")
except Exception as e:
print("An Exception accured!")
print(e)
sys.exit(1)
s.close()
