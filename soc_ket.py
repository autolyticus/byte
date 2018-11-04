import socket as s
import sys
import upload as u

class Exchange:
    def receive(self, host='0.0.0.0'):
        PORT_NUMBER = 7899
        SIZE = 1024
        try:
            host = s.gethostbyname(host)
        except:
            pass

        mySocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
        mySocket.bind((host, PORT_NUMBER))

        (data, addr) = mySocket.recvfrom(SIZE)
        data=data.decode('utf-8')
        downloader = u.TransferData()
        downloader.download_file(data)

    
    def send(self, server, link):
        SERVER_IP = server
        PORT_NUMBER = 7899
        SIZE = 1024
        print("Test client sending packets to IP {0}, via port {1}\n".format(
            SERVER_IP, PORT_NUMBER))

        mySocket = s.socket(s.AF_INET, s.SOCK_DGRAM)

        mySocket.sendto(link.encode('utf-8'), (SERVER_IP, PORT_NUMBER))

