from otpauth import OtpAuth
from time import sleep
import socket
global auth
auth = OtpAuth('secret')
def led(status):
    count=0
    if status == "good":
        while count < 10
            #gpio
            sleep(1)
            count=count+1
    elif status == "authfalse":
        while count < 4
            #gpio
            sleep(1)
            count=count+1
    elif status == "Falt":
        while True:
            #gpio
            sleep(1)
            #gpio
            sleep(1)
def respond(IP, msg):
    UDP_IP = IP
    UDP_PORT = 5006

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg, (UDP_IP, UDP_PORT))
def doorlock():
    led("good")
    print "The Door is now locked, Waiting for next request"
def doorunlock(OTP, IP):
    if auth.valid_totp(int(OTP)) == True:
        msg="OTP match Door Unlocked Unlocking for 10 seconds"
        print msg
        respond(IP,msg)
        doorlock()
    elif OTP=="failed":
        led("authfalse")
        print "user has failed auth"
    else:
        msg = "Somthing has gone wrong, Waiting for Admin"
        print msg
        led("Falt")
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
    print "hello"
    main()
