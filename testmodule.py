import socket
from otpauth import OtpAuth
auth = OtpAuth('secret')

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
MESSAGE = str(auth.totp())

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
