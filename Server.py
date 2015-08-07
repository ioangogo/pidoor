from otpauth import OtpAuth
from time import sleep
import socket
global auth
auth = OtpAuth('secret')

def respond(IP, msg):
    UDP_IP = IP
    UDP_PORT = 5006

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg, (UDP_IP, UDP_PORT))
def doorlock():
    print "The Door is now locked, Waiting for next request"
def doorunlock(OTP, IP):
    if auth.valid_totp(int(OTP)) == True:
        msg="OTP match Door Unlocked Unlocking for 10 seconds"
        #gpio stuff
        #return sucsess
        print msg
        respond(IP,msg)
        sleep(10)
        doorlock()
    else:
        msg = "OTP missmatch, failed attempt Your  ip address is being loged"
        print msg
        respond(IP,msg)
def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        doorunlock(data, addr[0])

if __name__ == '__main__':
    main()
