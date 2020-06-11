
import socket
import sys

PORT = 1234


def my_hex(bytes):
    return ' '.join(['%02X' % b for b in bytes])


def main(port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    while True:
        data = sock.recvfrom(4096)[0]
        print('<<< ' + my_hex(data))


if __name__ == '__main__':
    port = int(sys.argv[1])
    main(port)
