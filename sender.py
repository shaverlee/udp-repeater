
import socket
import random
import time
import sys


def my_hex(bytes):
    return ' '.join(['%02X' % b for b in bytes])


def random_data():
    num = random.randint(10, 100)
    return bytes([random.randint(0, 0xFF) for i in range(num)])


def main(port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    while True:
        data = random_data()
        print('>>> ' + my_hex(data))
        sock.sendto(data, ('127.0.0.1', port))
        time.sleep(1)


if __name__ == '__main__':
    port = int(sys.argv[1])
    main(port)
