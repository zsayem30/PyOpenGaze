import socket
import pickle
import time
from xml.sax.saxutils import escape

s = socket.socket()
host = '10.0.0.1'
port = 4242

s.connect((host, port))

print('Connected!')

# setup_msgs = {
# 	'timestamp': '<SET ID="ENABLE_SEND_TIME" STATE="1"/>\r\n',
# 	'pog_left': '<SET ID="ENABLE_SEND_POG_LEFT" STATE="1"/>\r\n',
# 	'pog_right': '<SET ID="ENABLE_SEND_POG_RIGHT" STATE="1"/>\r\n',
# 	'enable': '<SET ID="ENABLE_SEND_DATA" STATE="1"/>\r\n',
# }

def getMsg(prop):
	msg = f'<SET ID="{prop}" STATE="1"/>\r\n'
	return msg.encode(encoding='ascii', errors='xmlcharrefreplace')

# def parseGazeData(data):



while True:
	print('Sending command...')
	s.send(getMsg('ENABLE_SEND_TIME'))
	print('sent 1')
	s.send(getMsg('ENABLE_SEND_POG_LEFT'))
	print('sent 2')
	s.send(getMsg('ENABLE_SEND_POG_RIGHT'))
	print('sent 3')
	ack = s.recv(1024).decode()
	
	if ack[:4] == '<ACK':
		print('server acknowledged request!')
		break

	time.sleep(0.1)

s.send(getMsg('ENABLE_SEND_DATA'))

while True:
	try:
		msg = s.recv(1024)
		print(msg)
		time.sleep(1)
	except ConnectionResetError as e:
		print(e)
		s.connect((host, port))
