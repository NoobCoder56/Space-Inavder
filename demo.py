import socket
sock = socket.socket(socket.af_inet,socket.sock_stream)
ip = socket.gethostbyname('localhost')
sock.connect(('amazon.in',80))
cmd = 'get http://amazon.in http/1.0\r\n\r\n'.encode()
sock.send(cmd)
data = sock.recv(512)
print(data)