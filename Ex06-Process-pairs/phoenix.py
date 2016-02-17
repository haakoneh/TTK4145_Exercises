import os
import msgClass
import time

UDP_PORT = 20009
UDP_IP = "129.241.187.156"
buffer_size = 1024


def createBackup():
	os.system('python phoenix.py')


def main():
	msg = msgClass.MessageClass(1, UDP_PORT, UDP_IP, buffer_size)

	recvCount, prevRecvCount = 0, 0


	#passive backup loop
	while True:
		recvCount = int(msg.retrieveMsg())
		if(recvCount == 0):
			#Main has died
			createBackup()
			break

		prevRecvCount = recvCount

	counter = prevRecvCount

	#Active main loop
	while True:
		print counter
		counter += 1
		msg.setMsg(str(counter))
		msg.sendMsg()
		time.sleep(1)

main()

