import socket
from datetime import datetime

net = input("Enter the IP address (break to skip scan): ")

if net == 'break':
    pass
else:
    net1 = net.split('.')
    a = '.'

    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Enter the Starting Number: "))
    en1 = int(input("Enter the Last Number: "))
    en1 = en1 + 1
    t1 = datetime.now()


    def scan(addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr, 135))
        if result == 0:
            return 1
        else:
            return 0


    for ip in range(st1, en1):
        addr = net2 + str(ip)
        if scan(addr):
            print(addr, "is live")

    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)

ip_address = input('Enter IP address: ')
sock = socket.socket()
sock.connect((ip_address, 55000))

while True:
    command = input('Enter a command (type list for list, break for break): ')
    if command == 'break':
        break
    elif command == 'list':
        print('1. pork\n2.calc\n3.crash\n4.break\n5.list')
